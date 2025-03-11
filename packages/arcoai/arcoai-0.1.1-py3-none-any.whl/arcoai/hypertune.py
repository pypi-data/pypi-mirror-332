from sklearn.model_selection import GridSearchCV

class HyperparameterTuner:
    def __init__(self, model, param_grid, cv=3, scoring='accuracy'):
        self.model = model
        self.param_grid = param_grid
        self.cv = cv
        self.scoring = scoring

    def tune(self, X_train, y_train):
        grid_search = GridSearchCV(estimator=self.model, param_grid=self.param_grid, cv=self.cv, scoring=self.scoring)
        grid_search.fit(X_train, y_train)
        return grid_search.best_params_, grid_search.best_score_
