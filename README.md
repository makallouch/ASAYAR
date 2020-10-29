# ASAYAR

## Overview
Welcome to ASAYAR, the first public dataset dedicated for Latin (French) and Arabic Scene Text Detection in Highway panels. It comprises more than 1800 well-annotated images. The dataset was colleted from Moroccan Highway and it has been manually annotated. ASAYAR data can be used to develop and evaluate traffic signs detection and French or Arabic text detection in different languages.

## Annotation format
In the dataset, each instance's location is annotated by a rectangle bounding boxes. The bounding box can be denoted as `{XMIN, YMIN, XMAX, YMAX}`. An obejct has a class name denoted as CLASS. The global image information are defined as follows: FOLDER, **PATH**, **NAME**, and **SIZE**.
The following script shows an example of annotation : 
```
<annotation>
    <folder>FOLDER</folder>
    <filename>IMAGE_NAME</filename>
    <path>PATH</path>
    <source>
        <database>ASAYAR</database>
    </source>
    <size>
        <width>WIDTH</width>
        <height>HEIGHT</height>
        <depth>DEPTH</depth>
    </size>
    <object>
        <name>CLASS</name>
        <bndbox>
            <xmin>XMIN</xmin>
            <ymin>YMIN</ymin>
            <xmax>XMAX</xmax>
            <ymax>YMAX</ymax>
        </bndbox>
    </object>
    ...
</annotation>
```

## Dataset structure
```
Train or Test/
├── Traffic signs/
│   ├── Annotations/
│   │   ├── image_1.xml
│   │   └── ...
│   └── Images
│       ├── image_1.png
│       └── ...
│       
├── Text/
│   ├── Word Level/
│   │   ├── Annotations/
│   │   │   ├── image_1.xml
│   │   │   └── ...
│   │   └── Images/
│   │       ├── image_1.png
│   │       └── ...
│   └── Line Level/
│       ├── Annotations/
│       │   ├── image_1.xml
│       │   └── ...
│       └── Images/
│           ├── image_1.png
│           └── ...
└── Directional Symbols/
    ├── Annotations/
    │   ├── image_1.xml
    │   └── ...
    └── Images/
        ├── image_1.png
        └── ...
```

## Import data
To convert annotations from Voc pascal to txt format (`xmin,ymin,xmax,ymax,class`),


## Convert to text format
To convert annotations from Voc pascal to txt format (`xmin,ymin,xmax,ymax,class`) use `convert2txt.py`.

## Donwload

The images and their annotations are available here. [Download Link](https://vcar.github.io/ASAYAR/)

## Examples of Annotated Images
<img src="https://vcar.github.io/ASAYAR/images/image_895.png" width="700">



