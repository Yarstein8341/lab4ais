{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPKtsZS1oRmAk5M8Zfn5EtK"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":2,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"fINdCm_6MA2G","executionInfo":{"status":"ok","timestamp":1734885143186,"user_tz":-120,"elapsed":1325,"user":{"displayName":"Ярослав Білотіл","userId":"06797585363548962278"}},"outputId":"c1142105-8106-477e-ee99-4c2fb284ebd1"},"outputs":[{"output_type":"stream","name":"stdout","text":["Linear Regressor performance:\n","Mean absolute error = 3.58\n","Mean squared error = 20.31\n","Median absolute error = 2.99\n","Explained variance score = 0.86\n","R2 score = 0.86\n","\n","Linear regression prediction: [36.05286276]\n","Polynomial regression prediction: [41.08297799]\n","\n","Polynomial Regressor performance:\n","Mean absolute error = 67.99\n","Mean squared error = 88447.88\n","Median absolute error = 5.78\n","Explained variance score = -584.54\n","R2 score = -587.72\n"]}],"source":["import numpy as np\n","from sklearn import linear_model\n","import sklearn.metrics as sm\n","from sklearn.preprocessing import PolynomialFeatures\n","\n","# Завантаження даних з файлу\n","input_file = 'data_multivar_regr.txt'\n","data = np.loadtxt(input_file, delimiter=',')\n","X, y = data[:, :-1], data[:, -1]\n","\n","# Розбивка даних на навчальний та тестовий набори\n","num_training = int(0.8 * len(X))\n","num_test = len(X) - num_training\n","\n","X_train, y_train = X[:num_training], y[:num_training]\n","X_test, y_test = X[num_training:], y[num_training:]\n","\n","# Лінійна регресія\n","linear_regressor = linear_model.LinearRegression()\n","linear_regressor.fit(X_train, y_train)\n","\n","# Прогнозування результатів для тестового набору\n","y_test_pred = linear_regressor.predict(X_test)\n","\n","# Виведення метрик якості лінійної регресії\n","print(\"Linear Regressor performance:\")\n","print(\"Mean absolute error =\", round(sm.mean_absolute_error(y_test, y_test_pred), 2))\n","print(\"Mean squared error =\", round(sm.mean_squared_error(y_test, y_test_pred), 2))\n","print(\"Median absolute error =\", round(sm.median_absolute_error(y_test, y_test_pred), 2))\n","print(\"Explained variance score =\", round(sm.explained_variance_score(y_test, y_test_pred), 2))\n","print(\"R2 score =\", round(sm.r2_score(y_test, y_test_pred), 2))\n","\n","# Поліноміальна регресія\n","polynomial = PolynomialFeatures(degree=10)\n","X_train_transformed = polynomial.fit_transform(X_train)\n","X_test_transformed = polynomial.fit_transform(X_test)\n","\n","# Створення та навчання поліноміального регресора\n","poly_linear_model = linear_model.LinearRegression()\n","poly_linear_model.fit(X_train_transformed, y_train)\n","\n","# Прогнозування для вибіркової точки\n","datapoint = [[7.75, 6.35, 5.56]]\n","poly_datapoint = polynomial.fit_transform(datapoint)\n","\n","print(\"\\nLinear regression prediction:\", linear_regressor.predict(datapoint))\n","print(\"Polynomial regression prediction:\", poly_linear_model.predict(poly_datapoint))\n","\n","# Прогнозування результатів для тестового набору з використанням поліноміального регресора\n","y_test_pred_poly = poly_linear_model.predict(X_test_transformed)\n","\n","# Виведення метрик якості поліноміальної регресії\n","print(\"\\nPolynomial Regressor performance:\")\n","print(\"Mean absolute error =\", round(sm.mean_absolute_error(y_test, y_test_pred_poly), 2))\n","print(\"Mean squared error =\", round(sm.mean_squared_error(y_test, y_test_pred_poly), 2))\n","print(\"Median absolute error =\", round(sm.median_absolute_error(y_test, y_test_pred_poly), 2))\n","print(\"Explained variance score =\", round(sm.explained_variance_score(y_test, y_test_pred_poly), 2))\n","print(\"R2 score =\", round(sm.r2_score(y_test, y_test_pred_poly), 2))"]}]}