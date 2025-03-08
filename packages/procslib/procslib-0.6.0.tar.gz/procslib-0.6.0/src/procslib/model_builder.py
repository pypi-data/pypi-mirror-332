# src/procslib/model_builder.py
import hashlib

# ===== ADD YOUR MODELS BELOW =====
import logging
import os

from huggingface_hub import hf_hub_download

from procslib.config import get_config

logger = logging.getLogger(__name__)


def get_twitter_logfav_model():
    """A model trained for predicting Twitter log-favorites using AnimeAestheticInference.
    Takes an anime image as input and outputs the predicted log-scaled number of Twitter favorites.
    """
    from procslib.models import AnimeAestheticInference

    curr_org = get_config("HF_ORG")

    # Download the model checkpoint from the Hugging Face Hub
    checkpoint_path = hf_hub_download(
        repo_id=f"{curr_org}/{'aes-pred-convbase-twitter-logfav'}",
        filename="convbase_twitter_aes_logfav_full_v2cont3_e4_mae0.50.ckpt",
    )
    print(checkpoint_path)

    # Initialize the inference model
    return AnimeAestheticInference(checkpoint_path=checkpoint_path, column_name="twitter_logfav_score")


def get_weakm_v2_model():
    """A model trained for WeakM aesthetic predictions (v2) with low mean absolute error.
    输入anime图片, 输出预测的weakm v2 score (base score:10)
    """
    from procslib.models import AnimeAestheticInference

    curr_org = get_config("HF_ORG")

    # Download the model checkpoint from the Hugging Face Hub
    checkpoint_path = hf_hub_download(
        repo_id=f"{curr_org}/{'aes-pred-convbase-weakm-v2'}",
        filename="epoch=4,mae=0.0824,step=0.ckpt",
    )
    print(checkpoint_path)
    return AnimeAestheticInference(checkpoint_path=checkpoint_path, column_name="weakm_v2_score")


def get_weakm_v3_model():
    """A model trained for WeakM aesthetic predictions (v2) with low mean absolute error.
    输入anime图片, 输出预测的weakm v2 score (base score:10)
    """
    from procslib.models import AnimeAestheticInference

    curr_org = get_config("HF_ORG")

    # Download the model checkpoint from the Hugging Face Hub
    checkpoint_path = hf_hub_download(
        repo_id=f"{curr_org}/{'aes-pred-convbase-weakm-v3'}",
        filename="epoch=7,mae=0.2295,step=0.ckpt",
    )
    print(checkpoint_path)
    return AnimeAestheticInference(checkpoint_path=checkpoint_path, column_name="weakm_v3_score")


def get_siglip_aesthetic_model():
    """A Siglip-based aesthetic model for high-efficiency aesthetic predictions.
    输入anime图片, 输出预测的siglip aesthetic score
        https://github.com/discus0434/aesthetic-predictor-v2-5
    """
    from procslib.models import SiglipAestheticInference

    return SiglipAestheticInference(device="cuda", batch_size=32)


def get_pixiv_compound_score_model():
    """Aesthetic model trained on pixiv data (of the constructed pixiv compound aesthetic score)
    model at "https://bucket-public-access-uw2.s3.us-west-2.amazonaws.com/dist/compound_score_aesthetic_predictor/model.ckpt"
    """
    from procslib.models import PixivCompoundScoreInference

    # Download the model checkpoint from the Hugging Face Hub
    curr_org = get_config("HF_ORG")
    checkpoint_path = hf_hub_download(
        repo_id=f"{curr_org}/{'aes-pred-convtiny-pixiv-compound-larry'}",
        filename="pixiv_compound_aesthetic_convtiny_larry.ckpt",
    )
    print(checkpoint_path)
    return PixivCompoundScoreInference(model_path=checkpoint_path, column_name="pixiv_compound_score")


def get_complexity_ic9600_model():
    """A model trained for predicting image complexity using the IC9600 model.
    输入图片, 输出图片复杂度评分
    """
    from procslib.models import IC9600Inference

    # Download the model checkpoint from the Hugging Face Hub
    curr_org = get_config("HF_ORG")
    checkpoint_path = hf_hub_download(
        repo_id=f"{curr_org}/{'complexity-ic9600-model'}",
        filename="complexity_ic9600_ck.pth",
    )
    print(checkpoint_path)
    return IC9600Inference(model_path=model_path, device="cuda", batch_size=32)


def get_cv2_metrics_model():
    """Calculates OpenCV-based image metrics such as brightness, contrast, noise level, etc.
    输入图片, 输出图片质量评分
    """
    from procslib.models import OpenCVMetricsInference

    return OpenCVMetricsInference(device="cpu", batch_size=32)


def get_rtmpose_model():
    """A model trained for human pose estimation using RTMPose.
    输入图片, 输出人体姿势关键点
    """
    from procslib.models import RTMPoseInference

    # Download the model checkpoint from the Hugging Face Hub
    curr_org = get_config("HF_ORG")
    checkpoint_path = hf_hub_download(
        repo_id=f"{curr_org}/{'rtm-pose-model'}",
        filename="rtmpose-l_8xb256-420e_humanart-256x192-389f2cb0_20230611_e2e.onnx",
    )
    print(checkpoint_path)
    return RTMPoseInference(onnx_file=onnx_file, device="cuda")


def get_depth_model(**overrides):
    """Using "Intel/dpt-hybrid-midas" model for depth estimation and exports a 'depthness' score.
    输入图片, 输出图片深度分 (0.0-1.0, higher is more depth)
    """
    from procslib.models.depth_wrapper import DepthEstimationInference

    return DepthEstimationInference(
        **overrides,
    )


def get_q_align_quality_model(**overrides):
    """A model trained for predicting image quality using QAlign.
    输入图片, 输出图片质量评分
    """
    from procslib.models.q_align import QAlignAsyncInference

    return QAlignAsyncInference(task="quality", **overrides)


def get_q_align_aesthetics_model(**overrides):
    """A model trained for predicting image aesthetics using QAlign.
    输入图片, 输出图片美学评分
    """
    from procslib.models.q_align import QAlignAsyncInference

    return QAlignAsyncInference(task="aesthetics", **overrides)


def get_laion_watermark_model(**overrides):
    """A model trained for predicting watermarks using Laion.
    输入图片, 输出水印评分
    """
    from procslib.models.laion_watermark import LaionWatermarkInference

    return LaionWatermarkInference(**overrides)


def get_cached_clip_aesthetic_model(batch_size=32, **overrides):
    """Calculate and cache clip aesthetics embs and calcualtes the aesthetic scores and 0shot cls scores"""
    import unibox as ub

    from procslib.models.clip_aesthetic_cached import CachedClipAestheticInference, get_mlp_model
    from procslib.utils.utils import get_gpu_id_from_env

    # Load textual prompts (for CLIP similarity, if desired)
    clip_prompts = ub.loads("s3://bucket-external/misc/yada_store/configs/clip_prompts_list_full_v2.txt")

    # Instantiate MLPs using the updated get_mlp_model function.
    clip_mlp = get_mlp_model("kiriyamaX/clip-aesthetic")  # Regression MLP
    twitter_mlp = get_mlp_model("kiriyamaX/twitter-aesthetic-e20")  # Regression MLP
    twitter_v2_mlp = get_mlp_model("kiriyamaX/twitter-aesthetic-v2-e10")  # Regression MLP

    # For NSFW classification, let the state dict define the number of classes.
    nsfw_mlp = get_mlp_model("some-user/nsfw-v5", model_type="classification")

    mlp_configs = [
        (clip_mlp, "clip_aesthetic", "regression", {}),
        (twitter_mlp, "twitter_aesthetic", "regression", {}),
        (twitter_v2_mlp, "twitter_aesthetic_v2", "regression", {}),
        (nsfw_mlp, "nsfw", "classification", {0: "SFW", 1: "NSFW"}),
    ]

    device_id = get_gpu_id_from_env()
    random_hash = hashlib.sha1(os.urandom(8)).hexdigest()[:4]
    h5_path = f"./clip_cache_gpu{device_id}_{random_hash}.h5"

    config = {
        "prompts_list": clip_prompts,
        "mlp_configs": mlp_configs,
        "h5_path": h5_path,
        "device": "cuda",
        "batch_size": batch_size,
        "num_workers": 8,
    }
    config.update(overrides)
    return CachedClipAestheticInference(**config)


def get_vila_model():
    """A model trained for generating captions using VILA (Efficient-Large-Model/NVILA-15B)
    https://github.com/NVlabs/VILA

    输入图片, 输出描述
    """
    from procslib.models.vila_wrapper import VILAInference

    return VILAInference(model_path="Efficient-Large-Model/NVILA-15B", device="cuda", batch_size=1)


def get_jz_tagger_model(**overrides):
    """JzDanbooruTagger: multi-label classification + aesthetic score; knowledge cutoff ~early 2025"""
    from procslib.models.jz_tagger import JzDanbooruTaggerInference

    curr_org = get_config("HF_ORG")
    model_dir = f"hf://{curr_org}/jz-danbooru-tagger"
    return JzDanbooruTaggerInference(model_dir=model_dir, **overrides)


def get_aigc_classifier_model(**overrides):
    """A model for classifying AI-generated art vs. real images using incantor/aigc_real_cls.

    Finetuned on facebook/convnext-base-384-22k-1k.
    - https://huggingface.co/incantor/aigc_cls

    "on pixiv select by artist eval set":
    - Accuracy: 0.9621
    - Precision: 0.9459
    - Recall: 0.9811
    - F1-score: 0.9632
    """
    from procslib.models.hf_automodel_inference import HfAutomodelInference

    curr_org = get_config("HF_ORG")
    model_path = f"{curr_org}/aigc_cls"

    return HfAutomodelInference(
        model_path=model_path,
        task="classification",
        device=overrides.get("device", "cuda"),
        batch_size=overrides.get("batch_size", 32),
    )


def get_szh_image_category_model(**overrides):
    """A model for classifying image categories using HuggingFace model: szh/image_category_cls.
    输入图片, 输出对应类别.

    classifying image categories using HuggingFace model;

    Availabe categories:
    1. Animal
    2. Art
    3. character
    4. City
    5. Food
    6. Illustration
    7. Indoor
    8. Plant
    9. Product
    10. Scenery
    11. transportation

    """
    from procslib.models.hf_automodel_inference import HfAutomodelInference

    curr_org = get_config("HF_ORG")
    model_path = f"{curr_org}/image_category_cls"

    return HfAutomodelInference(
        model_path=model_path,
        task="classification",
        device=overrides.get("device", "cuda"),
        batch_size=overrides.get("batch_size", 32),
    )


def get_anime_real_cls_model(**overrides):
    """A model for classifying images as anime or real using "incantor/anime_real_cls".
    输入图片, 输出包含类别及置信度.

    Finetuned on google/vit-base-patch16-384.
    - https://mewtant-inc.sg.larksuite.com/docx/Z7VudRjfVot1xdxcgkQuQfiIsNd
    - https://huggingface.co/incantor/anime_real_cls

    Label 0: Anime Images
    Label 1: Real Images
    """
    from procslib.models.hf_automodel_inference import HfAutomodelInference

    curr_org = get_config("HF_ORG")
    model_path = f"{curr_org}/anime_real_cls"

    return HfAutomodelInference(
        model_path=model_path,
        task="classification",
        device=overrides.get("device", "cuda"),
        batch_size=overrides.get("batch_size", 32),
    )


def get_wdv3_timm_model(**overrides):
    """WDv3 Tagger using timm from SmilingWolf's HF repos.

    Args:
        repo_id: eg. SmilingWolf/wd-eva02-large-tagger-v3
        gen_threshold: Probability threshold for general tags.
        char_threshold: Probability threshold for character tags.
        device: "cuda" or "cpu".
        batch_size: Batch size for inference.
    """
    from procslib.models.wdv3_tagger_timm import WDV3TaggerTimmInference

    return WDV3TaggerTimmInference(**overrides)


def get_custom_image_model(**overrides):
    """A custom-trained image model from Hugging Face transformers supporting classification, regression, or ordinal tasks.
    Input: images, Output: predicted labels/values based on task type.
    Can be initialized with a Hugging Face model ID or a local folder path.

    Args:
        model_path (str): Either a Hugging Face model ID or a local folder path.
        task (str): Task type ('classification', 'regression', 'ordinal').
        device (str): Device to run inference on ('cuda' or 'cpu').
        batch_size (int): Batch size for inference.
    """
    from procslib.models.hf_automodel_inference import HfAutomodelInference

    default_model = "google/vit-base-patch16-224"  # Example base model
    model_path = overrides.get("model_path", default_model)
    task = overrides.get("task", "classification")  # Default to classification

    logger.info(f"Loading custom image model from {model_path} for task: {task}")

    return HfAutomodelInference(
        model_path=model_path,
        task=task,
        device=overrides.get("device", "cuda"),
        batch_size=overrides.get("batch_size", 32),
    )


def get_novelai_model(**overrides):
    """A wrapper for NovelAI's text-to-image API.
    输入文本提示, 输出生成的图像

    reads token from env: export NOVELAI_TOKEN="pst-yourTokenHere"
    """
    from procslib.models.novelai_wrapper import NovelAIInference

    # Try to get token from environment variable first
    persistent_token = os.environ.get("NOVELAI_TOKEN")

    # If token not in environment, try to get from config
    if not persistent_token:
        from procslib.config import get_config

        try:
            persistent_token = get_config("NOVELAI_TOKEN")
        except:
            # If still not found and no override provided, this will raise an error in the model class
            pass

    # Allow overriding the token and other parameters
    overrides_with_token = {"persistent_token": persistent_token, **overrides}

    return NovelAIInference(**overrides_with_token)


def get_pixai_tagger_model(**overrides):
    """A model that tags images using PixAI tagger models.
    输入图片, 输出图片标签
    """
    from procslib.models.pixai_tagger import PixAITaggerInference

    return PixAITaggerInference(**overrides)


MODEL_REGISTRY = {
    "twitter_logfav": get_twitter_logfav_model,
    "weakm_v2": get_weakm_v2_model,
    "weakm_v3": get_weakm_v3_model,
    "siglip_aesthetic": get_siglip_aesthetic_model,
    "pixiv_compound_score": get_pixiv_compound_score_model,
    "cv2_metrics": get_cv2_metrics_model,
    "complexity_ic9600": get_complexity_ic9600_model,
    "rtmpose": get_rtmpose_model,
    "depth": get_depth_model,
    "q_align_quality": get_q_align_quality_model,
    "q_align_aesthetics": get_q_align_aesthetics_model,
    "laion_watermark": get_laion_watermark_model,
    "clip_aesthetic": get_cached_clip_aesthetic_model,
    "vila": get_vila_model,
    "jz_tagger": get_jz_tagger_model,
    "aigc_classifier": get_aigc_classifier_model,
    "szh_image_category": get_szh_image_category_model,
    "anime_real_cls": get_anime_real_cls_model,
    "wdv3_tagger_timm": get_wdv3_timm_model,
    "custom_image": get_custom_image_model,
    "novelai": get_novelai_model,
    "pixai_tagger": get_pixai_tagger_model,
}


# ============ DO NOT EDIT BELOW THIS LINE ============


def get_model_keys():
    """Retrieves the keys and descriptions of the model registry.

    Returns:
        dict: A dictionary where keys are model names and values are descriptions.
    """
    return {key: func.__doc__.strip() if func.__doc__ else "no description" for key, func in MODEL_REGISTRY.items()}


def get_model(descriptor: str, **overrides):
    """Retrieves the actual model instance associated with the given descriptor.

    Args:
        descriptor (str): The model descriptor key in the MODEL_REGISTRY.

    Returns:
        object: The model instance.

    Raises:
        ValueError: If the descriptor is not found in MODEL_REGISTRY.
    """
    if descriptor not in MODEL_REGISTRY:
        raise ValueError(f"Descriptor '{descriptor}' not found in MODEL_REGISTRY.")
    return MODEL_REGISTRY[descriptor](**overrides)
