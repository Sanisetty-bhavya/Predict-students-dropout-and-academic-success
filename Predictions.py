df['Predictions'] = tree_classifier.predict(X)
predicted_class_distribution = df['Predictions'].value_counts()
print("Predicted Distribution:\n", predicted_class_distribution)
plt.figure(figsize=(3, 3))
plt.pie(predicted_class_distribution, labels=predicted_class_distribution.index, explode=[0.1] + [0] * (len(predicted_class_distribution) - 1), shadow=True, autopct="%0.2f%%")
plt.title('Predicted Class Distribution')
plt.legend()
plt.show()
actual_class_distribution = df['Target'].value_counts()
print("\nActual Distribution:\n", actual_class_distribution)
plt.figure(figsize=(3, 3))
plt.pie(actual_class_distribution, labels=actual_class_distribution.index, explode=[0.1] + [0] * (len(actual_class_distribution) - 1), shadow=True, autopct="%0.2f%%")
plt.title('Actual Class Distribution')
plt.legend()
plt.show()

test_predictions = tree_classifier.predict(X_test)
accuracy = accuracy_score(y_test, test_predictions)
classification_report_result = classification_report(y_test, test_predictions)
print(f"Test Set Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report_result)
