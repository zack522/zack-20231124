def funny_dialog():
    print("🎉 欢迎来到有趣的对话程序! 🎉")
    
    name = input("你叫什么名字? ")
    print(f"你好, {name}!")

    age = int(input("告诉我你的年龄: "))
    
    if age < 18:
        print("哇，你还真年轻！")
    elif 18 <= age <= 30:
        print("你正值青春年华！")
    elif 31 <= age <= 50:
        print("成熟稳重，正当壮年！")
    else:
        print("年龄不是问题，你依然年轻活力！")

    print("谢谢参与有趣的对话！")

# 运行有趣的对话程序
funny_dialog()
    
