from PIL import Image #从PIL中引入Image类
import argparse  #作用是用来管理命令行参数输入

#命令行输入参数处理
# 首先导入argparse模块，然后创建一个parser解析对象
# 再向该对象中添加要关注的命令行参数和选项，每一个add——argument方法对应\n
# 一个要关注的参数选项，然后调用parse——args进行解析，解析成功之后进行使用
parser = argparse.ArgumentParser()

parser.add_argument('file')  #输入文件
parser.add_argument('-o','--output')  #输出文件
parser.add_argument('--width',type=int,default=int(input('输入字符的宽')))#输出字符画宽
parser.add_argument('--height',type=int,default=int(input('输入字符的高')))#输出字符画高

#获取参数
args=parser.parse_args()

IMG=args.file
WIDTH=args.width
HEIGHT=args.height
OUTPUT=args.output

#定义一个ascii列表，为了让图片的灰度和字符对应
ascii_char=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#将256灰度映射到70个字符上
def get_char(r,g,b,alpha=256):
	if alpha == 0:  #如果灰度是0，则说明没有图片
		return ' '
	length=len(ascii_char) #计算字符的长度
	gray=int(0.2126*r+0.7152*g+0.0722*b) #把RGB值转化为灰度值

	unit=(256.0+1)/length
	return ascii_char[int(gray/unit)]  #表明灰度值和字符的对应关系


if __name__=='__main__':  #如果是本程序调用，则执行以下程序
	im=Image.open(IMG)   #打开图片
	im=im.resize((WIDTH,HEIGHT),Image.NEAREST)  #更改图片的显示比例

	txt=""  #txt初始值为空

	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt+= get_char(*im.getpixel((j,i)))   #把图片按照横纵坐标解析成rgb以及alpha这几个参数，然后调用get_char函数，把对应的图片转为灰度值
		txt+='\n' #换行


	num=input("输入保存的图片名(避免重复)：")
	print(txt)  #打印


	#字符画输出到文件
	if OUTPUT:
		with open(OUTPUT,'w') as f:
			f.write(txt,i)

	else:
		with open(" %s.txt"%num,'w')as f :
			f.write(txt,i)
	
     #通过自定义output的文件名，确保了多次转换的时候原来的字符画不被覆盖
     #通过自定义宽，高实现不同图片的美观性 
