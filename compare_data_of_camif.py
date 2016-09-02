#!/usr/bin/python2.7
import sys
import struct
# -*- coding: UTF-8 -*-
y_list = []
u_list = []
v_list = []
frame_size = 1920*6
LINE = 6
COL = 1920
def store_yuv422p_to_file(file, y_offset, u_offset, v_offset):

    for pix in y_list[y_offset: y_offset + frame_size] :
        #print pix, "pix"
        data = struct.pack('B', int(pix, 16))
        #print data, "data"
        file.write(data)
        #print type(pix)
        #data = hex(int(pix, 16))
        #print data, "data"

    for pix in u_list[u_offset : u_offset + frame_size/2]:
        data = struct.pack('B', int(pix, 16))
        #print data, "data"
        file.write(data)
    for pix in v_list[v_offset : v_offset + frame_size/2]:
        data = struct.pack('B', int(pix, 16))
        #print data, "data"
        file.write(data)
    file.close()

def store_yuv422sp_to_file(file, y_offset, u_offset, v_offset):
    for pix in y_list[y_offset: y_offset + frame_size] :
        #print pix, "pix"
        data = struct.pack('B', int(pix, 16))
        #print data, "data"
        file.write(data)

    pos_tag = v_offset
    for pix in u_list[u_offset : u_offset + frame_size/2]:

        data = struct.pack('B', int(pix, 16))
        #print data, "data"
        file.write(data)
        tmp = v_list[pos_tag]
        data = struct.pack('B', int(tmp, 16))
        file.write(data)
        pos_tag = pos_tag +1
    file.close()

def store_yuv422interlaced_to_file(file, y_offset, u_offset, v_offset):
    y_pos = y_offset
    v_pos = v_offset

    for pix in u_list[u_offset: u_offset + frame_size/2] :
        tmp = y_list[y_pos]
        data = struct.pack('B', int(tmp, 16))
        file.write(data)
        #print pix, "pix"
        data = struct.pack('B', int(pix, 16))
        #print data, "data"
        file.write(data)

        tmp = y_list[y_pos+1]
        data = struct.pack('B', int(tmp, 16))
        file.write(data)

        tmp = v_list[v_pos]
        data= struct.pack('B', int(tmp, 16))
        file.write(data)

        y_pos = y_pos + 2
        v_pos = v_pos + 1
    file.close()

def store_yuv420sp_to_file(file, y_offset, u_offset, v_offset):

    #first store all Y
    for pix in y_list[y_offset: y_offset + frame_size] :
        #print pix, "pix"
        data = struct.pack('B', int(pix, 16))
        #print data, "data"
        file.write(data)
    #then store uv
    uv_line_pos = u_offset
    uv_pos = u_offset
    for eachline in range(0, LINE, 1):
        print eachline, "eachline"
        if (eachline % 2 == 0):
            continue
        for eachcol in range(0, COL/2, 1):
            #print eachcol, "eachcol"
            tmp = u_list[uv_line_pos + eachcol]
            #print tmp, "tmp value"
            data = struct.pack('B', int(tmp, 16))
            file.write(data)
            tmp = v_list[uv_line_pos+ eachcol]
            data = struct.pack('B', int(tmp, 16))
            file.write(data)

        uv_line_pos = u_offset + (eachline+1)*COL/2
        print uv_line_pos, "uv_line_pos"

def store_yuv420sp_to_file_hsub_and_vsub(file, y_offset, u_offset, v_offset):

    u_pos = u_offset
    v_pos = v_offset
    sub_ulist = []
    sub_vlist = []
    #first store all Y
    for pix in y_list[y_offset: y_offset + frame_size] :
        #print pix, "pix"
        data = struct.pack('B', int(pix, 16))
        #print data, "data"
        file.write(data)

    pos_tag = u_offset
    #u or v has frame_size/4 datas
    #422 subsample to 420
    #first sub sample u to sub_ulist
    #print "ulist len:", len(u_list)
    print "u_pos:", u_pos
    for index in range(0, frame_size/2, 4):

        u_pos = index
        print u_pos, "u_pos"
        print index, "index"
        tmp = u_list[u_pos]
        sub_ulist.append(tmp)
        tmp = u_list[u_pos + 1]
        sub_ulist.append(tmp)
    #sub sample v to sub_ylist
    for index in range(2, frame_size/2, 4):
        v_pos =  index
        tmp = v_list[v_pos]
        sub_vlist.append(tmp)
        tmp = v_list[v_pos + 1]
        sub_vlist.append(tmp)
    #last store sub u,v to file
    sub_vpos = 0
    for pix in sub_ulist :
        #first sub_u
        data = struct.pack('B', int(pix,16))
        file.write(data)
        #then sub_v
        tmp = sub_vlist[sub_vpos]
        data  = struct.pack('B', int(tmp,16))
        file.write(data)
        tmp_pos = sub_vpos + 1

    file.close()

def generate_frame_data(offset, fmt, store):

    y_offset = frame_size*(offset - 1)
    u_offset = frame_size*(offset - 1)/2
    v_offset = frame_size*(offset -1)/2

    name ="%s%s_%s%d" % (fmt, store, "frame", offset)
    file = open(name, "wb")

    if (fmt == "yuv422" and store == "p"):
        store_yuv422p_to_file(file, y_offset, u_offset, v_offset)
    elif (fmt == "yuv422" and store == "sp"):
        store_yuv422sp_to_file(file, y_offset, u_offset, v_offset)
    elif (fmt == "yuv422" and store == "int"):
        store_yuv422interlaced_to_file(file, y_offset, u_offset, v_offset)
    elif (fmt == "yuv420" and store == "sp"):
        store_yuv420sp_to_file(file, y_offset, u_offset, v_offset)

def generate_yuv_list(fobj, y_list, u_list, v_list) :

   flines = fobj.readlines()
   count = 0
   for eachLine in flines:
       eachLine = eachLine[0:-1]
       count = count + 1
       if (count % 2 != 0) : #is Y

            y_list.append(eachLine)

       elif (count % 4 == 0): # is cR
            #print 'CR',  eachLine,
            v_list.append(eachLine)

       else :
            #print "%s" % 'CB', type(data), data,
            u_list.append(eachLine)


#command: which frame
if __name__ == "__main__" :

    if "help" == sys.argv[1]:
        print "the usage:\n"
        print "./script_name offset fmt store"
        print "example:"
        print "./compare_data_of_camif.py 1 yuv422 sp"
    else :

        if len(sys.argv) < 3 :
            print "the argument number is not correct!"
            exit(1)

        in_file = open("camif8.hex", 'rb')

        generate_yuv_list(in_file, y_list, u_list, v_list)
        #print y_list
        #print u_list
        #print v_list
        generate_frame_data(int(sys.argv[1]), sys.argv[2], sys.argv[3])

        in_file.close()
        print "well done!!"