import flet as ft
import flet_permission_handler as fph
try:
    from . import core
    from .version import version
except ImportError:
    import core
    from version import version

__version__ = version

aboutmsg="""能给个Star吗，求求了😭  
或者在爱发电给一点小小的资金支持！"""

def page(page: ft.Page):
    # 关于窗口
    def about(e=None):
        dialog = ft.AlertDialog(
           modal=True,
           title=ft.Text("关于"),
           content=ft.Container(  # 添加尺寸限制容器
               content=ft.Column([
                   ft.Row([
                       ft.Image("/icon.png",width=40, height=40),
                       ft.Markdown(f"**All Of Resources {__version__}**  \n[Github](https://github.com/SystemFileB/all-of-resources) | [爱发电](https://afdian.com/a/systemfileb)",on_tap_link=lambda e: page.launch_url(e.data))
                   ]),
                   ft.Markdown(aboutmsg,on_tap_link=lambda e: page.launch_url(e.data)),
               ], scroll=ft.ScrollMode.HIDDEN),
               width=250,  # 固定宽度
               height=100  # 固定高度
           ),
           on_dismiss=lambda e: page.close(dialog),
           actions=[ft.TextButton("关闭", on_click=lambda e: page.close(dialog))]
        )
        page.open(dialog)
    
    page.title=f"All Of Resources {__version__}"
    page.vertical_alignment=ft.MainAxisAlignment.START
    bar = ft.AppBar(
        title=ft.Row([
            ft.Text(f"All Of Resources {__version__}"),
            ft.Container(expand=True),  # 新增中间弹性容器
            ft.IconButton(
                icon=ft.Icons.INFO_OUTLINE,
                on_click=about,
                tooltip="关于",
            )
        ], 
        expand=True,
        alignment=ft.MainAxisAlignment.START),  # 设置对齐方式
    )
    page.add(bar)

    # 检查是否信息收集完毕
    def check(e=None):
        nonlocal minecraftdir_old
        result=core.check(minecraftdir_text.value,version_box.value,outputdir_text.value)
        if minecraftdir_old!=minecraftdir_text.value:
            if result[0]:
                version_box.options=[ft.dropdown.Option(i) for i in result[0]]
                version_box.value=result[0][0]
        if result[1]:
            logtext.value=result[2]
            start_button.disabled=False
        minecraftdir_old=minecraftdir_text.value
        page.update()
    
    def task(e=None):
        def callback(progress,msg):
            logtext.value=msg
            progressbar.value=progress/2000
            page.update()
        def runtask():
            def close(e=None):
                page.close(dialog)
                progressbar.value=0
                page.update()

            result=core.task(minecraftdir_text.value,version_box.value,outputdir_text.value,callback)
            if result[0]=="E":
                icon=ft.Icons.ERROR_OUTLINE
                logtext.value=result[1]
            elif result[0]=="I":
                icon=ft.Icons.INFO_OUTLINE
                logtext.value="All Of Resources FLUTTER EDITION!\n给个Star awa"
            dialog=ft.AlertDialog(modal=True,
                                  title=ft.Text("All Of Resources"),
                                  content=ft.Row([ft.Icon(icon),ft.Text(result[1])]),
                                  actions=[ft.TextButton("关闭", on_click=close)],
                                  on_dismiss=close
            )
            page.open(dialog)
            start_button.disabled=False
        
        start_button.disabled=True
        page.update()
        page.run_thread(runtask)
    
    # 文件选择器
    TO_MINECRAFTDIR=0
    TO_OUTPUTDIR=1
    pickTo=TO_MINECRAFTDIR
    def pick_dir_event(e: ft.FilePickerResultEvent):
        if pickTo==TO_MINECRAFTDIR:
            minecraftdir_text.value=e.path
        elif pickTo==TO_OUTPUTDIR:
            outputdir_text.value=e.path
        check()

    def filedialog(ftype,title):
        nonlocal pickTo
        # 给权限！
        check_status=premission.check_permission(fph.PermissionType.STORAGE)
        if type(check_status) == fph.PermissionStatus and check_status == fph.PermissionStatus.DENIED and premission.request_permission(fph.PermissionType.STORAGE):
            return
        pickTo=ftype
        file_picker.get_directory_path(title)
    file_picker=ft.FilePicker(on_result=pick_dir_event)

    # 我要权限！
    premission=fph.PermissionHandler()

    page.overlay.append(file_picker)
    page.overlay.append(premission)

    # 构建界面
    minecraftdir_text=ft.TextField(label=".minecraft目录位置", expand=1, on_change=check)  # 添加expand让输入框填充剩余空间
    minecraftdir_select_button=ft.ElevatedButton(text="...",on_click=lambda e: filedialog(TO_MINECRAFTDIR,"选择.minecraft目录"))
    minecraftdir = ft.Row([minecraftdir_text, minecraftdir_select_button])
    minecraftdir_old=minecraftdir_text.value

    version_box=ft.Dropdown(label="版本",width=int(float(page.width)) if page.width else 400)

    outputdir_text=ft.TextField(label="输出目录位置", expand=1, on_change=check)  # 添加expand让输入框填充剩余空间
    outputdir_select_button=ft.ElevatedButton(text="...",on_click=lambda e: filedialog(TO_OUTPUTDIR,"选择解压路径"))
    outputdir = ft.Row([outputdir_text, outputdir_select_button])

    progressbar=ft.ProgressBar(value=0)

    logtext=ft.Text(value="All Of Resources FLUTTER EDITION!\n给个Star awa\n\n注意：解压路径需要使用空文件夹")

    start_button=ft.FloatingActionButton(
        icon=ft.Icons.DOWNLOAD,
        tooltip="开始",
        disabled=True,
        on_click=task
    )

    page.add(minecraftdir,version_box,outputdir,progressbar,logtext,start_button)



def main():
    ft.app(
        target=page,
        use_color_emoji=True
    )

if __name__=="__main__":
    main()