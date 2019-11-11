'''
1.修改os.chdir的路径，为本py文件所在的路径，可以相对路径，也可以用绝对路径
2.修改path的路径，用相对（os.chdir）路径表示要转化的xml文件所在的位置
3.修改xml_df.to_csv('person_train.csv', index=None)的文件名，注意不要忘记.csv结尾

'''




import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


#os.chdir是本py的路径，相对或者绝对路径均可
os.chdir('/Users/junbin/Documents/GitHub/TensorFlow/models/research/object_detection/images')
#path是要转化的xml文件所在的位置
path = './train/'

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    image_path = path
    xml_df = xml_to_csv(image_path)
    #下面一行修改成生成的csv的文件名，改成跟标签同名即可，注意不能省略.csv
    xml_df.to_csv('galsses_train.csv', index=None)
    print('Successfully converted xml to csv.')


main()