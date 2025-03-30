from transformers import AutoModelForCausalLM, Trainer, TrainingArguments
import torch

def fine_tune_model(model_name, dataset_path):
    model = AutoModelForCausalLM.from_pretrained(model_name)
    
    training_args = TrainingArguments(
        output_dir="models/",
        per_device_train_batch_size=4,
        save_steps=10,
        save_total_limit=2,
        num_train_epochs=3
    )

    trainer = Trainer(model=model, args=training_args)
    trainer.train()

    model_path = f"models/{model_name}-fine-tuned"
    model.save_pretrained(model_path)

    return model_path
