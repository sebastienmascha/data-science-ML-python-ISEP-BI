# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
datafinitiElectronicsProductData = dataiku.Dataset("DatafinitiElectronicsProductData")
datafinitiElectronicsProductData_df = datafinitiElectronicsProductData.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

def editCategoryTitle(categoryTitle):
    switcher = {
    'Accessories,Portable Power Banks,Portable Chargers/Power Packs,Cell Phones & Accessories,Cell Phones,Portable Battery Packs,Cell Phone Accessories,Cell Phone Batteries & Power,Batteries & Battery Packs,cell,Power,Chargers & Cradles': "Phone Accessories",
    'Audio & Video Accessories,TV Mounts,TV Accessories & Parts,Electronics,A/V Presentation,Accessories & Supplies,TV Ceiling & Wall Mounts': "Television",
    'Auto & Tires,Auto Electronics,Car Speakers and Subwoofers,10\\ Car Subwoofer,Car Subwoofers,All Car Subwoofers,Car Electronics & GPS,Car Audio,Car Subwoofers & Enclosures,Component Subwoofers,Consumer Electronics,Vehicle Electronics & GPS,eBay Motors,Parts & Accessories,Car Electronics,Subwoofers & Enclosures,Subwoofers,Electronics,Car & Vehicle Electronics': "Car Accessories",
    'Auto & Tires,Auto Electronics,Car Speakers and Subwoofers,6.5\\ Car Speakers,All Car Speakers & Subwoofers,Car Electronics & GPS,Car Audio,Car Speakers,Electronics,Car & Vehicle Electronics,Car Electronics,Speakers,Coaxial Speakers': "Car Accessories",
    'Computers & Tablets,Computer Accessories & Peripherals,Laptop Accessories,Laptop Chargers & Adapters,Computers,Electronics,Computer Accessories': "Computer Accessories",
    'Computers,Desktops Workstations,Desktop Computers,Desktop Computers wbeszexzzxeteywxtzby,Computers & Tablets,Desktop & All-in-One Computers,All Desktops,Electronics,Computers & Accessories,Desktops,Towers,Computers/Tablets & Networking,Desktops & All-In-Ones,PC Desktops & All-In-Ones': "Computers",
    'Computers,Internal Hard Drives,Internal Drives,Drives, Storage & Blank Media,Computers & Accessories,Hard Drives (HDD, SSD & NAS),Computer Accessories & Peripherals,Internal Hard Disk Drives,Electronics,Hard Drives & Storage,Drives Storage,Computers/Tablets & Networking,Computer Components,Computers & Tablets,Data Storage': "Phone Accessories",
    'Computers,Memory (RAM),Computers & Accessories,Computer Components,Memory,Memory Upgrades,Electronics,Computers & Tablets,Computer Cards & Components,Laptop Memory': "Computer Electronics",
    'Computers,Mice & Mice Pads,Computer Accessories,Computer Accessories & Peripherals,Keyboards, Mice & Joysticks,Electronics,Gaming Mice & Mice Pads,Accessories,Mice & Keyboards,Video Games,Gaming Mice,Computers & Tablets,Mice,Wireless & Bluetooth Mice': "Computer Accessories",
    'Computers,Networking,Home Networking & Connectivity,Electronics,See more Novatel Jetpack MiFi 6620l Hotspot 4G LTE Veri...,Cell Phones,Cell Phone Accessories,Mobile Broadband,Mobile Broadband Devices,Access Points, Hubs & Switches,Computers/Tablets & Networking,Verizon Hotspots,Mobile Hotspots,Cell Phones & Accessories,Cell': "Computer Accessories",
    'Computers,Portable Battery Packs yxdasxffaabvrfusya,Portable Chargers/Power Packs,Computers & Accessories,Computer Accessories,Computer Accessories & Peripherals,Portable Battery Packs ccbdtucwsuccsbzvxsect,Frys,Electronics,Portable Battery Packs,Cell Phones,Cell Phone Accessories,Cell Phone Batteries & Power,Batteries,Surge Protectors,Surge Protectors, Power Strips,PC Computers,Consumer Electronics,Mobile Power,Power Accessories,Multipurpose Batteries & Power,Rechargeable Batteries,Portable Battery Packs bcxsstqzbavv,Power, Cooling Racks': "Computers",
    'Computers,Wireless Networking rwtaqbstbwzzteq,Networking,Computers & Accessories,Wireless Adapters Cards,Wireless Networking,Electronics,Networking Products,Network Adapters,Networking Cables & Accessories,USB Network Adapters': "Computers",
    'Desktop Memory,Computers/Tablets & Networking,Memory (RAM),Computer Components & Parts,Computers & Accessories,Computer Components,Memory (RAM,Memory,Electronics,Computers & Tablets,Computer Cards & Components': "Computer Accessories",
    'Electronics,Accessories & Supplies,Audio & Video Accessories,Remote Controls & Accessories,TV & Video,TV Accessories,Remote Controls,TVs Entertainment,General Accessories,Accessories,Consumer Electronics,TV, Video & Home Audio,TV, Video & Audio Accessories,See more Logitech Harmony Ultimate One IR Remote With C...,TV Remote Controls,TV & Home Theater,TV & Home Theater Accessories,Universal Remote Controls,Stereo Accessories,Electronics Features': "Television Accessories",
    'Electronics,CD Players & Digital Media Receivers,Car Electronics,Motors,Marine Stereos,CD Players,Fishing,Car Audio,Automotive,Car & Vehicle Electronics,Car Stereo Receivers,Digital Media Receivers,Outdoor Sports,Marine Electronics,Car Electronics & GPS': "Television Accessories",
    'Electronics,Cameras & Camcorders,All Camcorders,Home, Garage & Office,Pet Supplies & Technology,Pet Cameras & Technology,Wearable Pet Cameras,Computers & Accessories,Computer Accessories & Peripherals,Audio & Video Accessories,Webcams,Housewares,Pet Cameras,Dog,Training Aids,Training & Behavior,Networking,Computers,Routers,pet,Security & Surveillance,Surveillance Video Equipment,Security Monitors & Displays': "Camera",
    'Electronics,Car & Vehicle Electronics,Car Electronics,Car Audio,Speakers,Coaxial Speakers,Car Electronics & GPS,Car Speakers,6\\ x 8\\ Car Speakers': "Car Accessories",
    'Electronics,Computers,Computer Accessories,Blank Media,Accessories & Supplies,Data Cartridges,Cameras & Photo,Camera & Photo Accessories,Camcorder Tapes & Discs,Cameras & Camcorders,Camcorder Accessories,Blank DVDs & Tapes,Consumer Electronics,TV, Video & Home Audio,TV, Video & Audio Accessories,Other TV, Video & Audio Accs,Mini DVs,Accessories,Audio Cassettes': "Electronics",
    "Electronics,Computers,Computer Accessories,Keyboards, Mice & Joysticks,Keyboards,All Keyboards,Computers & Accessories,Computer Accessories & Peripherals,Keyboards, Mice & Accessories,Computers & Tablets,iPad & Tablet Accessories,Tablet Cases, Covers & Keyboard Folios,Computer Peripherals,Keyboards Accessories,Computers Features,Cases, Covers & Keyboard Folios,Name Brands,Microsoft,Microsoft Surface,Microsoft Surface Accessories,Microsoft Surface Cases & Covers,Microsoft Surface Tablets,Frys,Tablets,Cases": "Computer Accessories",
    'Electronics,Home Audio & Theater,Home Audio,All Home Speakers,Speaker Systems,Audio,Bluetooth & Wireless Speakers,All Bluetooth & Wireless Speakers,Stereos,Speakers': "Television Accessories",
    'Electronics,Home Audio & Theater,Home Theater,Home Theater Systems,Consumer Electronics,Portable Audio & Headphones,iPod, Audio Player Accessories,Audio Docks & Mini Speakers,TVs Entertainment,Tabletop Audio,Mini Hi-Fi Systems,Audio,Home Audio,Stereo Shelf Systems,Frys,Shelf Systems,CD Players,Portable Audio': "Television Accessories",
    'Electronics,Portable Audio & Video,Home Audio & Theater,Home Audio,All Home Speakers,Speaker Systems,Consumer Electronics,TV, Video & Home Audio,Home Theater Systems,See more Black BOYTONE Bt-210f 30 Watt FM Radio Bluetoo...,Audio,Stereos,Speakers,Cell,MP3 Player Accessories,Portable Bluetooth Speakers,See more BOYTONE Bt-210f Bluetooth Wireless Speaker Mp3...': "Audio",
    'Electronics,Portable Audio,Auto & Tires,Auto Electronics,Car Receivers,All In-Dash Stereos,Car & Vehicle Electronics,Car Electronics,Car Video,In-Dash DVD & Video Receivers,Car Audio,Car Stereo Receivers,All Car Stereo Receivers,Automotive': "Car Accessories",
    'Electronics,Portable Audio,MP3 Accessories,All Portable Speakers,Audio,Docks, Radios & Boomboxes,Radios,Portable Audio & Video,Shortwave Radios': "Audio",
    'Headphones,Bluetooth Headphones,All Headphones,Electronics,Audio,Mobile': "Audio",
    'Headphones,Bluetooth Headphones,On-Ear Headphones,Electronics,Bluetooth Headphones rydyqsaxrbrdyuquyetsrydxefvucsr,Audio,Mobile': "Audio",
    'Headphones,Electronics,Over-Ear Headphones,Audio,Over-Ear & On-Ear Headphones': "Audio",
    'Home Theater Systems,Portable Audio & Video,Electronics,MP3 & MP4 Player Accessories,Home Audio,Home Audio & Theater,All Home Stereos,Audio,Stereo Shelf Systems': "Television Accessories",
    'In-Wall & In-Ceiling Speakers,Electronics,In-Ceiling Speakers,TVs Entertainment,Speakers,Home Audio & Theater,All Home Speakers,Install Outdoor Speakers wbdadzefwwsbvcrtwtvxqqdxsqdwtdtrwt,Home Audio,Install Outdoor Speakers,In-Wall and In-Ceiling Speakers,Audio,all electronics': "Audio",
    'Internal Solid State Drives,Computers & Accessories,Computer Accessories & Peripherals,Electronics,Computers & Tablets,Hard Drives & Storage,Data Storage': "Computers",
    'LED & LCD TVs,All TVs,Refurbished TVs,TV & Video,Electronics,Shop TVs by Type,Television & Video,Televisions,TVs Entertainment': "Television Accessories",
    'Mobile,Headphones,Bluetooth Headphones,Electronics,Audio,Over-Ear & On-Ear Headphones,Over-Ear Headphones,Shop Headphones by Type,Over-Ear and On-Ear Headphones,Frys': "Audio",
    'Office,Office Technology,Phones & Accessories,Headsets & Accessories,Walmart for Business,Office Electronics,Phones,Home, Garage & Office,Telephones & Communication,Special Needs Telephones,Categories,Big Button & Amplified Telephones,Electronics Features,Connected Home & Housewares,Phones Video Conferencing,Analog Phones Accessories,Phone Accessories,Collaboration IP Telephony': "Phone",
    'Office,Projectors & Presentation Equipment,Audio Visual Presentation,TV Stands, Mounts & Furniture,Projector Mounts Accessories,Projector Mounts & Screens,Projector Mounts,Electronics,TV & Home Theater,Office Technology,Mounts Carts,Mounting Plates,A/V Presentation,Networking Products,Powerline Network Adapters,Network Adapters': "Electronics",
    'Outdoor Speakers,Electronics Features,Electronics,TVs Entertainment,Speakers,Install Outdoor Speakers,Home Audio,Home Audio & Theater,Audio,All Home Speakers': "Electronics",
    'Photography,Photography Bags Cases,Camera Bags,Backpacks,Backpacks ffvzrevebzuqvcddwzzxeuwva,Cameras & Camcorders,Digital Camera Accessories,Camera Bags, Cases & Straps,Camera Backpacks,Electronics,Camera Accessories,Camera Bags & Cases,Computers Features,Bag & Case Accessories,Camera & Photo Features,Camera & Photo,Bags & Cases,Camera Cases,Outdoor Recreation,Hiking Daypacks,Backpacking Packs': "Camera",
    'Portable Bluetooth Speakers,Audio Docks & Mini Speakers,Bluetooth & Wireless Speakers,Portable Audio & Headphones,Portable Audio & Video,Electronics,Portable Audio,Portable Wireless & Bluetooth Speakers,Speakers,Home Audio & Theater,Wireless Home Speakers,Mobile,iPod, Audio Player Accessories,Consumer Electronics,Mobile Bluetooth Speakers,Wireless and Bluetooth Speakers,UNNAV,Portable Speakers & Docks,Audio,Mobile Speakers,All Bluetooth & Wireless Speakers': "Audio",
    'Portable Bluetooth Speakers,Audio Docks & Mini Speakers,Bluetooth & Wireless Speakers,Portable Audio & Headphones,Portable Audio & Video,Electronics,TVs Entertainment,Speakers,Home Audio & Theater,Wireless Home Speakers,All Home Speakers,iPod, Audio Player Accessories,Consumer Electronics,Wireless Speakers,Wireless & Multiroom Audio,Wireless and Bluetooth Speakers,Home Audio,Portable Speakers & Docks,Audio,Wireless Multiroom Speakers,Wireless Multi-Room Speakers': "Audio",
    'Portable Bluetooth Speakers,Audio Docks & Mini Speakers,Used:TV Entertainment,Bluetooth & Wireless Speakers,Portable Audio & Headphones,Used:Portable Audio,Portable Audio & Video,Frys,Electronics,Sony SRS-HG1,Used:Speakers,Home Audio & Theater,Wireless Home Speakers,All Home Speakers,Mobile,iPod, Audio Player Accessories,Consumer Electronics,Mobile Bluetooth Speakers,Audio Speakers,Home Audio,Portable Speakers & Docks,Audio,Mobile Speakers': "Audio",
    'Portable Bluetooth Speakers,Bluetooth & Wireless Speakers,Portable Audio & Video,Electronics,Portable Speakers & Docks,Audio': "Audio",
    'Portable Bluetooth Speakers,Bluetooth & Wireless Speakers,Portable Audio & Video,Electronics,Portable Speakers & Docks,Audio,All Bluetooth & Wireless Speakers': "Audio",
    'Portable Bluetooth Speakers,Stereos,Computers,Bluetooth & Wireless Speakers,Computer Accessories,Speaker Systems,Portable Audio & Video,Electronics,Portable Audio,Portable Wireless & Bluetooth Speakers,Speakers,Home Audio & Theater,Wireless and Bluetooth Speakers,Portable Speakers & Docks,Wireless & Portable Bluetooth Speakers,Audio,Computer Speakers': "Audio",
    'Satellite Radio,Satellite Radios,Car & Vehicle Electronics,Car Satellite Radios,Frys,Electronics,Car Electronics,Audio,SIRIUS XM Satellite Radio,Car Audio,Car Electronics & GPS': "Radio",
    'Speaker Separates,Center Channel Speakers,Electronics,TVs Entertainment,Speakers,Home Audio,Center-Channel Speakers,Audio,Speaker Separates baesfadqwexxbctqsw': "Audio",
    'Surround Speakers,Electronics Features,Surround Sound Systems,Frys,Electronics,All Home Theater Systems,TVs Entertainment,Speakers,Home Audio & Theater,Home Electronics,TV Sound Systems rxxbwxxcscxuvutetd,Home & Kitchen Features,Home Theater Systems,Audio Speakers,TV Sound Systems,Home Audio,Home Theater,Electrical,Audio': "Audio",
    'Surround Speakers,TV, Video & Home Audio,Surround Sound Systems,Electronics,All Home Theater Systems,TVs Entertainment,Speakers,Consumer Electronics,Home Theater Systems,TV Sound Systems,Audio & Home Theatre,Home Audio,Audio': "Audio",
    'TV & Video,Media Streaming Players,New Technology,Frys,Electronics,Streaming Media Players,Television & Video,TVs Entertainment,TV & Home Theater,Internet TV Broadcasters,Streaming Media,All Streaming Media Players': "Television",
    'TV, Video & Home Audio,Receivers,Electronics,TVs Entertainment,Compact & Shelf Stereos,Consumer Electronics,Home Audio Stereos, Components,Audio & Home Theatre,Receivers & Amplifiers,Home Audio Components,Home Audio,CD Players Changers,Audio,Compact Radios & Stereos,Stereo Shelf Systems': "Television",
    'stone products,electronics,Parts & Accessories,brick manufacturing,landmark stone,Car Electronics,brick manufacturing process,eBay Motors,natural stone,brick designs,Digital Media Receivers,Car Stereo Receivers,Vehicle Electronics & GPS,brick,Electronics Features,Video In-Dash Units w/o GPS,Car Video,thin brick,Car Audio In-Dash Units,Car Audio,Consumer Electronics,brick sizes,glen gery,manufactured stone,Car Video Units W/out GPS/Nav,Apple CarPlay Receivers,In-Dash with GPS,brick colors,Car Electronics & GPS': "Electronics"
                    }

    return switcher.get(categoryTitle, 'Electronics')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
datafinitiElectronicsProductData_df['categories'] = datafinitiElectronicsProductData_df.apply(lambda x: editCategoryTitle(x['categories']), axis=1)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#len(datafinitiElectronicsProductData_df['imageURLs'][0].split(','))
def countImageURLs(imageURLs) :
    return len(imageURLs.split(','))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
datafinitiElectronicsProductData_df['numberImages'] = datafinitiElectronicsProductData_df.apply(lambda x: countImageURLs(x['imageURLs']), axis=1)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
preProcessing_df = datafinitiElectronicsProductData_df # For this sample code, simply copy input to output


# Write recipe outputs
preProcessing = dataiku.Dataset("PreProcessing")
preProcessing.write_with_schema(preProcessing_df)