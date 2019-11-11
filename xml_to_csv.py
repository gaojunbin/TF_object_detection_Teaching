import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

#下面两行修改成自己存放.xml文件的路径，相对于xml_to_csv.py的路径即可，或者绝对路径
os.chdir('./train/xml')
path = './train/xml'

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
    xml_df.to_csv('glasses.csv', index=None)
    print('Successfully converted xml to csv.')


main()