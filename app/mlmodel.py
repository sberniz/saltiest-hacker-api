import joblib
model2 = joblib.load('tree_reg.pkl')
pipeline = joblib.load('sklearn_pipeline_tree.pkl')

def predict_text(text, model = model2):
    xtemp = pipeline.transform([text])
    predictions = model2.predict(xtemp)
    print(predictions)
    return predictions
preds = predict_text("I hate all this all of you")
print(preds[0])