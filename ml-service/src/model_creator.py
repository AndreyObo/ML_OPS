from src.train_models.train_classifier import create_model


create_model('UCI_Credit_Card.csv', 'default.payment.next.month', 'model_payment_next_month')