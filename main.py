import customtkinter as ctk
from modules.deceive_ai import DeceiveAIFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("赛博朋克功能平台")
        self.geometry("800x600")

        # 设置赛博朋克主题
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # 网格布局 (1x2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 创建侧边栏
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="功能模块", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.deceive_ai_button = ctk.CTkButton(self.sidebar_frame, text="欺骗 AI", command=self.deceive_ai_button_event)
        self.deceive_ai_button.grid(row=1, column=0, padx=20, pady=10)

        # 创建主内容区域
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        # 初始化时显示欢迎信息
        self.welcome_label = ctk.CTkLabel(self.main_frame, text="欢迎使用赛博朋克功能平台", font=ctk.CTkFont(size=24))
        self.welcome_label.pack(pady=50, padx=50)

        # 存储当前的模块界面
        self.current_module_frame = None

    def switch_module(self, module_frame_class):
        # 清理主内容区域
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # 如果存在旧的模块界面，销毁它
        if self.current_module_frame:
            self.current_module_frame.destroy()

        # 创建新的模块界面实例
        self.current_module_frame = module_frame_class(self.main_frame)
        self.current_module_frame.pack(fill="both", expand=True)

    def deceive_ai_button_event(self):
        self.switch_module(DeceiveAIFrame)

if __name__ == "__main__":
    app = App()
    app.mainloop()
