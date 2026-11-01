import torch


def probe_shapes():
    print("[*] Loading I-JEPA (ViT-H/14)...")

    # load official pretrained weights from FAIR repo
    model = torch.hub.load("facebookresearch/ijepa", "ijepa_vith14")
    model.eval()

    # batch_size, channels, height, width
    x = torch.randn(2, 3, 224, 224)

    with torch.no_grad():
        out = model(x)
        pooled = out.mean(dim=1) if out.ndim == 3 else out

    print(f"[+] Patch tokens shape : {out.shape}")
    print(f"[+] Pooled vector shape : {pooled.shape}")


if __name__ == "__main__":
    probe_shapes()