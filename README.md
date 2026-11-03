<div align="center">

# AI Security Defense Lab

**Hands-on exercises in hardening AI/ML systems: secrets, IAM scope and unsafe model loading.**

![Type educational lab](https://img.shields.io/badge/Type-educational_lab-7C3AED?style=for-the-badge) ![Python 3](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Cloud AWS IAM](https://img.shields.io/badge/Cloud-AWS_IAM-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![Models Hugging Face](https://img.shields.io/badge/Models-Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=white)

</div>

## Tech stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,aws,docker&perline=10" alt="Tech stack" />
</p>

## Lab map

```mermaid
flowchart TB
    L["Defense lab\nfictional MedVitals AI / DataForge ML systems"] --> S["Secrets hygiene\nconfig.py reads env vars\n.env.example only"]
    L --> I["Least-privilege IAM\ndeploy-role-policy.json"]
    L --> M["Level 2: model security\nlevel-2-model-security/model_loader.py"]
    M --> R{{"Risk: pickle.load on a downloaded .pkl\ncan execute attacker code"}}
    R --> F["Fix: safe formats such as safetensors,\npinned revisions, hash verification,\nsandboxed loading"]
```

## What each part teaches

| Path | Topic |
|---|---|
| `config.py`, `.env.example` | Secrets are loaded from environment variables, never committed. |
| `deploy-role-policy.json` | Review an IAM policy for over-broad actions and `Resource: "*"`. |
| `level-2-model-security/model_loader.py` | Intentionally unsafe example: it downloads a `.pkl` model and calls `pickle.load`, which can run attacker-controlled code if the file is malicious. |

> The systems in this lab (MedVitals AI, DataForge ML) are fictional. The loader in `level-2-model-security` is a deliberately vulnerable example, so do not reuse it in real projects.

---

