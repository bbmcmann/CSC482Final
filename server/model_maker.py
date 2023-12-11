import experiences_model

# IMPORTANT NOTE: if the bullet points training changes the models may not work anymore and might have to be retrained


# FORMAT: Each item is the settings for a new model
# ( PATH, NUM_EPOCHS )

batch_to_train_param_list = [
                    (".\\pytorch_models\experience_model_Maker100.pth", 100),
                    (".\\pytorch_models\experience_model_Maker50.pth", 50),
                    ]

already_trained_param_list = [(".\\pytorch_models\experience_model_Maker100.pth", 100),
                    (".\\pytorch_models\experience_model_Maker50.pth", 50)]


# test all models in train_param_list
def test_models():
    print("____TESTING ALL____")
    for settings in already_trained_param_list:
        print("\n\t\tTESTING: " + settings[0][17:] + "\n")
        experiences_model.test_model(settings[0], 15)


# train all models in train_param_list
def train_models():
    print("____TRAINING ALL____")
    for settings in batch_to_train_param_list:
        print("TRAINING SETTINGS: " + str(settings))
        experiences_model.build_experience_model(settings[0], settings[1])


if __name__ == '__main__':
    # train_models()

    test_models()
