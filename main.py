import customtkinter as ctk
from modules.deceive_ai import DeceiveAIFrame
import json
from PIL import Image
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- 主题和外观设置 ---
        self.load_theme("themes/cyberpunk.json")
        ctk.set_appearance_mode("Dark")

        self.title("赛博朋克功能平台")
        self.geometry("800x600")

        # --- 设置背景图片 ---
        self.setup_background("assets/background.jpg")

        # --- 网格布局 (1x2) ---
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- 创建侧边栏 ---
        # 设置为透明，以显示背景
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0, fg_color="transparent")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="功能模块", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.deceive_ai_button = ctk.CTkButton(self.sidebar_frame, text="欺骗 AI", command=self.deceive_ai_button_event)
        self.deceive_ai_button.grid(row=1, column=0, padx=20, pady=10)

        # --- 创建主内容区域 ---
        # 设置为透明
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        # 初始化时显示欢迎信息
        self.welcome_label = ctk.CTkLabel(self.main_frame, text="欢迎使用赛博朋克功能平台", font=ctk.CTkFont(size=24), fg_color="transparent")
        self.welcome_label.pack(pady=50, padx=50)

        # 存储当前的模块界面
        self.current_module_frame = None

    def load_theme(self, theme_file):
        """从 JSON 文件加载并应用颜色主题。"""
        try:
            if os.path.exists(theme_file):
                with open(theme_file, "r") as f:
                    ctk.set_default_color_theme(json.load(f))
            else:
                # 如果找不到主题文件，则使用默认的蓝色主题
                print(f"警告: 主题文件 '{theme_file}' 未找到，使用默认主题。")
                ctk.set_default_color_theme("blue")
        except Exception as e:
            print(f"加载主题失败: {e}")
            ctk.set_default_color_theme("blue")

    def setup_background(self, image_path):
        """设置窗口的背景图片。"""
        if not os.path.exists(image_path):
            print(f"警告: 背景图片 '{image_path}' 未找到。")
            return

        try:
            bg_image = ctk.CTkImage(Image.open(image_path), size=(800, 600))
            bg_label = ctk.CTkLabel(self, image=bg_image, text="")
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            # 将背景标签置于最底层
            bg_label.lower()
        except Exception as e:
            print(f"设置背景图片失败: {e}")


    def switch_module(self, module_frame_class):
        # 清理主内容区域
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if self.current_module_frame:
            self.current_module_frame.destroy()

        # 创建新的模块界面实例，并设置为透明
        self.current_module_frame = module_frame_class(self.main_frame, fg_color="transparent")
        self.current_module_frame.pack(fill="both", expand=True)

    def deceive_ai_button_event(self):
        self.switch_module(DeceiveAIFrame)

if __name__ == "__main__":
    app = App()
    app.mainloop()
