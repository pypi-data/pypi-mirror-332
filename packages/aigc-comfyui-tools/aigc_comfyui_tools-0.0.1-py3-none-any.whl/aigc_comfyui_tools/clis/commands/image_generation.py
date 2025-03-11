import click
from aigc_comfyui_tools.api.image_generation import ImageGeneration


@click.command('image_generation')
@click.option('--server', "-s", default="http://localhost:8188", help='SSL要用https, 本地用http')
@click.option('--text', "-t", default="masterpiece best quality girl, with a cat.", help='提示词')
@click.option('--api_json_path', "-p", default="./data/jsonfile/image_generation.json", help='API JSON File')
@click.option('--dst_dir', "-d", default="./tmp", help='生成的图片保存目录')

def cli(server, *args, **kwargs):
    """文件重命名。
    aigc_comfyui_tools image_generation -s "http://10.1.1.29:8180" -p "./data/jsonfile/image_generation.json"
    """
    print("ComfyUI Server: {}".format(server))
    tex2image = ImageGeneration(server)
    tex2image(*args, **kwargs)
    print("Images saved: {}".format(kwargs["dst_dir"]))
