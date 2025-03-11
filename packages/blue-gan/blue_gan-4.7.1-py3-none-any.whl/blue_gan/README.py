import os

from blue_objects import file, README

from blue_gan import NAME, VERSION, ICON, REPO_NAME


items = README.Items(
    [
        {
            "name": "PyTorch-GAN",
            "marquee": "https://github.com/eriklindernoren/PyTorch-GAN/raw/master/assets/logo.png",
            "description": "Code base.",
            "url": "https://github.com/eriklindernoren/PyTorch-GAN",
        },
        {
            "name": "What is a GAN?",
            "marquee": "https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2021/11/11/ML-6149-image025.jpg",
            "url": "https://aws.amazon.com/what-is/gan/",
        },
    ]
)


def build():
    return README.build(
        items=items,
        path=os.path.join(file.path(__file__), ".."),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
