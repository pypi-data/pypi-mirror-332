"""集成构建配置项"""
import argparse
import os, sys
from lbkit.log import Logger
from lbkit.misc import load_yml_with_json_schema_validate, TARGETS_DIR

log = Logger("build_config")


class Config(object):
    """集成构建的配置项"""
    def __init__(self, args = None):
        parser = self.arg_parser()
        args = parser.parse_args(args)

        # 配置项
        self.manifest = os.path.join(os.getcwd(), args.manifest)
        # 配置项目录
        self.work_dir = os.path.dirname(self.manifest)
        sys.path.append(self.work_dir)
        # 是否从源码构建
        self.from_source = args.from_source
        # 是否打印详细信息
        self.verbose = True if os.environ.get("VERBOSE", False) else False
        # 编译类型
        self.build_type = args.build_type
        # conan中心仓
        self.remote = args.remote

        if not os.path.isfile(self.manifest):
            raise FileNotFoundError(f"File {args.manifest} not exist")

        # 编译主机配置项
        self.profile_build = args.profile_build
        # 编译目标配置项
        self.profile_host = args.profile

        # conan.lock options
        self.using_lockfile = args.lockfile
        self.update_lockfile = args.update_lockfile
        self.target = args.target

        # 设置并创建构建所需目录
        log.info("Work dir: %s", self.work_dir)
        self.code_path = os.getcwd()
        self.temp_path = os.path.join(self.code_path, ".temp")
        self.output_path = os.path.join(self.temp_path, "output")
        self.download_path = os.path.join(self.temp_path, "download")
        self.tool_path = os.path.join(self.temp_path, "tools")
        # conan组件打包目录
        self.conan_install = []
        self.mnt_path = os.path.join(self.temp_path, "mnt_path")
        self.rootfs_img = os.path.join(self.output_path, "rootfs.img")
        # rootfs、uboot和kernel关键文件路径
        self.uboot_bin = None
        self.linux_bin = None
        self.rootfs_tar = None
        os.makedirs(self.temp_path, exist_ok=True)
        os.makedirs(self.tool_path, exist_ok=True)
        os.makedirs(self.output_path, exist_ok=True)
        os.makedirs(self.download_path, exist_ok=True)
        # 制作rootfs时需要strip镜像，所以需要单独指定stip路径
        self.strip = "strip"

    @staticmethod
    def target_list():
        targets = {}
        dirname = os.path.join(TARGETS_DIR)
        for file in os.listdir(dirname):
            if not file.endswith(".yml"):
                continue
            tgt_file = os.path.join(TARGETS_DIR, file)
            targets[file] = tgt_file
        return targets

    @staticmethod
    def arg_parser():
        """返回配置项支持的参数"""
        parser = argparse.ArgumentParser(description="Build LiteBMC", formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument("-m", "--manifest", help="Specify the manifest.yml, ignored when -l is specified.", default="./manifest.yml")
        parser.add_argument("-s", "--from_source", help="Build from source", action="store_true")
        parser.add_argument("-pr", "--profile", help="Apply the specified profile to the host machine", default="litebmc.ini")
        parser.add_argument("-pr:b", "--profile_build", help="Apply the specified profile to the build machine", default="default")
        parser.add_argument("-bt", "--build_type", type=str, choices=['debug', 'release', 'minsize'], help="Set the build type", default="debug")
        parser.add_argument("-r", "--remote", help="specified conan server", default="litebmc")
        parser.add_argument("-l", "--lockfile", help="using conan.lock", action="store_true")
        parser.add_argument("-ul", "--update_lockfile", help="update conan.lock", action="store_true")
        targets = Config.target_list()
        target_help = "build target:"
        for tgt, _ in targets.items():
            target_help += "\n* " + tgt[:-4]
        parser.add_argument("-t", "--target", help=target_help, default="default")
        return parser

    def get_manifest_config(self, key: str, default=None):
        """从manifest中读取配置"""
        manifest = self.load_manifest()
        keys = key.split("/")
        for k in keys:
            manifest = manifest.get(k, None)
            if manifest is None:
                return default
        return manifest

    def load_manifest(self):
        """加载manifest.yml并验证schema文件"""
        template = {}
        template["code_path"] = self.code_path
        template["temp_path"] = self.temp_path
        template["download_path"] = os.path.join(self.download_path)
        return load_yml_with_json_schema_validate(self.manifest, "/usr/share/litebmc/schema/pdf.v1.json", **template)

    def set_build_type(self, value):
        self.build_type = value

    def deal_conf(self, config_dict):
        """
        处理Target级别的配置"target_config"
        当Config类有set_xxx类方法时，则可以在target文件中配置xxx
        """
        if not config_dict or not isinstance(config_dict, dict):
            return
        for key, conf in config_dict.items():
            try:
                method = getattr(self, f"set_{key}")
                method(conf)
            except Exception as e:
                raise Exception(f"目标 config 无效配置: {key}") from e
