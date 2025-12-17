'''加载模型（Qwen2-1.5B 或 LLaMA3）

加载数据（你可以先用一个 toy dataset）

使用 Trainer 训练一个 epoch'''
import os
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
)

def main():
    model_name = "hfl/chinese-bert-wwm-ext"  # 先用一个小中文BERT

    # 1. 加载数据（CLUE tnews）
    dataset = load_dataset("clue", "tnews")
    train_ds = dataset["train"].select(range(2000))   # 为了快，先取2000条
    valid_ds = dataset["validation"].select(range(500))

    # 2. 加载 tokenizer 和 model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(
        model_name,
        num_labels=15,
    )

    def preprocess(examples):
        return tokenizer(
            examples["sentence"], 
            truncation=True,
            padding="max_length",
            max_length=128,
        )

    train_ds = train_ds.map(preprocess, batched=True)
    valid_ds = valid_ds.map(preprocess, batched=True)

    train_ds = train_ds.remove_columns(
        [c for c in train_ds.column_names if c not in ["input_ids", "token_type_ids", "attention_mask", "label"]]
    )
    valid_ds = valid_ds.remove_columns(
        [c for c in valid_ds.column_names if c not in ["input_ids", "token_type_ids", "attention_mask", "label"]]
    )

    train_ds.set_format("torch")
    valid_ds.set_format("torch")

    # 3. 定义训练参数
    training_args = TrainingArguments(
        output_dir="./outputs/tnews-minimal",
        per_device_train_batch_size=16,
        per_device_eval_batch_size=32,
        learning_rate=2e-5,
        num_train_epochs=1,
        evaluation_strategy="epoch",
        save_strategy="no",
        logging_steps=50,
        load_best_model_at_end=False,
    )

    # 4. 定义 Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=valid_ds,
    )

    # 5. 开始训练
    trainer.train()
    eval_metrics = trainer.evaluate()
    print("Eval metrics:", eval_metrics)

if __name__ == "__main__":
    main()
