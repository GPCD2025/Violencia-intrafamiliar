"""
Este script realiza la optimización de hiperparámetros para modelos de clasificación multietiqueta
 (Regresión Logística, Random Forest y Gradient Boosting) utilizando GridSearchCV. 
 Se definen espacios de búsqueda para cada modelo y se ejecuta la búsqueda de los mejores 
 parámetros mediante validación cruzada. Finalmente, se evalúan los modelos con métricas 
 como precisión, recall, F1-score y pérdida de Hamming.
"""

param_grid_logreg = {
    'estimator__C': [0.1, 1, 10],
    'estimator__penalty': ['l1', 'l2'],
    'estimator__solver': ['liblinear', 'saga']
}

param_grid_rf = {
    'estimator__n_estimators': [50, 100, 200],
    'estimator__max_depth': [None, 10, 20],
    'estimator__min_samples_split': [2, 5, 10]
}

param_grid_gb = {
    'estimator__n_estimators': [50, 100, 200],
    'estimator__learning_rate': [0.01, 0.1, 1],
    'estimator__max_depth': [3, 5, 7]
}

models = {
    'Logistic Regression': (MultiOutputClassifier(LogisticRegression()), param_grid_logreg),
    'Random Forest': (MultiOutputClassifier(RandomForestClassifier()), param_grid_rf),
    'Gradient Boosting': (MultiOutputClassifier(GradientBoostingClassifier()), param_grid_gb)
}

for model_name, (model, param_grid) in models.items():
    print(f"Training {model_name}...")
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    print(f"Best parameters for {model_name}: {grid_search.best_params_}")
    print(f"Best score for {model_name}: {grid_search.best_score_}")

    y_pred = grid_search.predict(X_test)
    
    # Evaluacion de metricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='micro')
    recall = recall_score(y_test, y_pred, average='micro')
    f1 = f1_score(y_test, y_pred, average='micro')
    hamming = hamming_loss(y_test, y_pred)

    print(f"Accuracy for {model_name}: {accuracy}")
    print(f"Precision for {model_name}: {precision}")
    print(f"Recall for {model_name}: {recall}")
    print(f"F1-score for {model_name}: {f1}")
    print(f"Hamming Loss for {model_name}: {hamming}")