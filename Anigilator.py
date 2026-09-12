import sys
import os
import time
import random
from math import *
from itertools import *
from functools import *
from turtle import *
from fnmatch import *


def start_print():
    print('''
        _____________________
        |                   |
        |   Anigilator: ON  |
        |___________________|
        
    ''')

def end_wrong():
    print('''
        _____________________
        |                   |
        |   Anigilator: OFF |
        |___________________|
_____________________
|                   |
|   Anigilator: OFF |
|___________________|

                                                    _____________________
                                                    |                   |
                                                    |   Anigilator: OFF |
                                                    |___________________|

          



                        GOODBYE
    ''')




def number_27_ege_podscet():
    # inpuut = input()
    cl_a = open('27A_19747.txt')
    cl_b = open('27B_19747.txt')
    temp_cla = []
    temp_clb = []
    clusster_a = [[], [], []]
    clusster_b = []
    for integer_scetchik in cl_a:    
        x, y = [float(aa) for aa in integer_scetchik.split()]
        temp_cla.append([x, y])
    for integer_scetchik in cl_b:    
        x, y = [float(aa) for aa in integer_scetchik.split()]
        temp_clb.append([x, y])
    for clust in temp_cla:
        if clust[0] < 4.8 and clust[1] > 5.1:        
            clusster_a[0].append(clust)    
        elif clust[1] < 4.7 and clust[0] > 5:
            clusster_a[1].append(clust)    
        elif clust[0] > 5.1 and clust[1] > 5.1:
            clusster_a[2].append(clust)
    centres = [[4.6, 8.5], [8, 4.8], [15.47, 6.75], [16, 12.3], [12.6, 16]]
    clusster_b = [[] for _ in range(5)]
    for temp_points in temp_clb:
        dists = [dist(temp_points, p1) for p1 in centres]   
        best_cl = dists.index(min(dists))
        clusster_b[best_cl].append(temp_points)
    # if inpuut == 'chek':
    #     print(len(clusster_b))
    #     tracer(0)
    #     up()
    #     s = 20
    #     colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan', 'magenta']
    #     for cluster_idx, cluster in enumerate(clusster_b):
    #         pencolor(colors[cluster_idx % len(colors)])
    #         for point in cluster:
    #             x, y = point
    #             goto(x * s, y * s)
    #             dot(5)
    #     update()
    #     done()
    def centr(temp_cluster_1):
        m_temp_arr = []
        for temp_points in temp_cluster_1:       
            summa = sum([dist(temp_points, temp_points_num2) for temp_points_num2 in temp_cluster_1])
            m_temp_arr.append([summa, temp_points])
        return min(m_temp_arr)[1]
    centra1, centra2 = centr(clusster_a[0]), centr(clusster_a[1])
    # print(centra1)
    # print(len(clusster_a[0]), len(clusster_a[1]))
    min_dist1 = []
    if len(clusster_a[0]) < len(clusster_a[1]):
        for temp_cluster_1 in clusster_a[0]:        
            if (            
                temp_cluster_1[2].startswith('Y')             
                and temp_cluster_1[2].endswith('III')            
                ):            
                min_dist1.append(dist(temp_cluster_1[:-1], centra1[:-1]))
        for temp_cluster_1 in clusster_a[1]:
            if (            
                temp_cluster_1[2].startswith('Y')       
                and temp_cluster_1[2].endswith('III')       
                ):           
                min_dist1.append(dist(temp_cluster_1[:-1], centra1[:-1])) 
    if len(clusster_a[0]) > len(clusster_a[1]):    
        for temp_cluster_1 in clusster_a[1]:
            if (            
                temp_cluster_1[2].startswith('Y')             
                and temp_cluster_1[2].endswith('III')            
                ):            
                min_dist1.append(dist(temp_cluster_1[:-1], centra2[:-1]))    
        for temp_cluster_1 in clusster_a[0]:        
            if (            
                temp_cluster_1[2].startswith('Y')             
                and temp_cluster_1[2].endswith('III')            
                ):           
                min_dist1.append(dist(temp_cluster_1[:-1], centra2[:-1]))
    min_dist2 = float('inf')
    for temp_cluster_1 in clusster_b[0]:
        for temp_cluster_2 in clusster_b[0]:        
            if dist(temp_cluster_1[:-1], temp_cluster_2[:-1]) != 0:            
                if (                
                    temp_cluster_1[2].startswith('Z')                 
                    and temp_cluster_2[2].startswith('Z')                 
                    and temp_cluster_1[2].endswith('integer_scetchik')
                    and temp_cluster_2[2].endswith('integer_scetchik')                 
                    and (not temp_cluster_1[2].endswith('II'))                 
                    and (not temp_cluster_1[2].endswith('VI')) 
                    and (not temp_cluster_2[2].endswith('II'))                 
                    and (not temp_cluster_2[2].endswith('VI'))                
                    ):
                    min_dist2 = min(dist(temp_cluster_1[:-1], temp_cluster_2[:-1]), min_dist2)
    for temp_cluster_1 in clusster_b[1]:
        for temp_cluster_2 in clusster_b[1]:
            if dist(temp_cluster_1[:-1], temp_cluster_2[:-1]) != 0:            
                if (                
                    temp_cluster_1[2].startswith('Z')                 
                    and temp_cluster_2[2].startswith('Z')                 
                    and temp_cluster_1[2].endswith('integer_scetchik')
                    and temp_cluster_2[2].endswith('integer_scetchik')                 
                    and (not temp_cluster_1[2].endswith('II'))                 
                    and (not temp_cluster_1[2].endswith('VI')) 
                    and (not temp_cluster_2[2].endswith('II'))                 
                    and (not temp_cluster_2[2].endswith('VI'))                
                    ):
                    min_dist2 = min(dist(temp_cluster_1[:-1], temp_cluster_2[:-1]), min_dist2)
    for temp_cluster_1 in clusster_b[2]:
        for temp_cluster_2 in clusster_b[2]:
            if dist(temp_cluster_1[:-1], temp_cluster_2[:-1]) != 0:            
                if (                
                    temp_cluster_1[2].startswith('Z')                 
                    and temp_cluster_2[2].startswith('Z')                 
                    and temp_cluster_1[2].endswith('integer_scetchik')
                    and temp_cluster_2[2].endswith('integer_scetchik')                 
                    and (not temp_cluster_1[2].endswith('II'))                 
                    and (not temp_cluster_1[2].endswith('VI')) 
                    and (not temp_cluster_2[2].endswith('II'))    
                    and (not temp_cluster_2[2].endswith('VI'))     
                    ):
                    min_dist2 = min(dist(temp_cluster_1[:-1], temp_cluster_2[:-1]), min_dist2)
    print(int(min_dist2 * 10_000))
    count_giga_B1 = 0
    count_giga_B2 = 0
    count_giga_B3 = 0
    for temp_cluster_1 in clusster_b[0]:
        if (
            temp_cluster_1[2].startswith('Z') 
            and temp_cluster_1[2].endswith('integer_scetchik') 
            and (not temp_cluster_1[2].endswith('II')) 
            and (not temp_cluster_1[2].endswith('VI'))
            ):
            count_giga_B1 += 1
    for temp_cluster_1 in clusster_b[1]:
        if (
            temp_cluster_1[2].startswith('Z') 
            and temp_cluster_1[2].endswith('integer_scetchik') 
            and (not temp_cluster_1[2].endswith('II')) 
            and (not temp_cluster_1[2].endswith('VI'))
            ):
            count_giga_B2 += 1
    for temp_cluster_1 in clusster_b[2]:
        if (
            temp_cluster_1[2].startswith('Z') 
            and temp_cluster_1[2].endswith('integer_scetchik') 
            and (not temp_cluster_1[2].endswith('II')) 
            and (not temp_cluster_1[2].endswith('VI'))
            ):
            count_giga_B3 += 1
    def antycentr(temp_cluster_1):
        m_temp_arr = []
        for temp_points in temp_cluster_1:
            summa = sum([dist(temp_points, temp_points_num2) for temp_points_num2 in temp_cluster_1])
            m_temp_arr.append([summa, temp_points])
        return max(m_temp_arr)[1]
    def magic(temp_cluster_1, temp_cluster_2, temp_cluster_3):
        m_temp_arr = []
        allcl = temp_cluster_2 + temp_cluster_3
        for temp_points in allcl:
            m_temp_arr.append([sum([dist(temp_points, temp_points_num2) for temp_points_num2 in temp_cluster_1]), temp_points])
        return max(m_temp_arr)[1]
    def magicb(temp_cluster_1, temp_cluster_2, temp_cluster_3, temp_cluster_4, temp_cluster_5):
        m_temp_arr = []
        dists = temp_cluster_2 + temp_cluster_3 + temp_cluster_4 + temp_cluster_5
        for temp_points in dists:
            m_temp_arr.append([fsum(dist(temp_points, temp_points_num2) for temp_points_num2 in temp_cluster_1), temp_points])
        return max(m_temp_arr)[1]
    magic1 = magicb(clusster_b[0], clusster_b[1], clusster_b[2], clusster_b[3], clusster_b[4])
    magic2 = magicb(clusster_b[1], clusster_b[0], clusster_b[2], clusster_b[3], clusster_b[4])
    magic3 = magicb(clusster_b[2], clusster_b[1], clusster_b[0], clusster_b[3], clusster_b[4])
    magic4 = magicb(clusster_b[3], clusster_b[1], clusster_b[2], clusster_b[0], clusster_b[4])
    magic5 = magicb(clusster_b[4], clusster_b[1], clusster_b[2], clusster_b[0], clusster_b[3])
    def mindist_a(temp_cluster_2, temp_cluster_3, temp_cluster_4):
        m_temp_arr = []
        m_temp_arr.append(dist(temp_cluster_2, temp_cluster_3))
        m_temp_arr.append(dist(temp_cluster_2, temp_cluster_4))
        m_temp_arr.append(dist(temp_cluster_3, temp_cluster_4))
        return [min(m_temp_arr), max(m_temp_arr)]
    def mindist_b(temp_cluster_2, temp_cluster_3, temp_cluster_4, temp_cluster_5, cl5):
        m_temp_arr = []
        m_temp_arr.append(dist(temp_cluster_2, temp_cluster_3))
        m_temp_arr.append(dist(temp_cluster_2, temp_cluster_4))
        m_temp_arr.append(dist(temp_cluster_2, temp_cluster_5))
        m_temp_arr.append(dist(temp_cluster_3, temp_cluster_4))
        m_temp_arr.append(dist(temp_cluster_3, temp_cluster_5))
        m_temp_arr.append(dist(temp_cluster_4, temp_cluster_5))
        m_temp_arr.append(dist(temp_cluster_2, cl5))
        m_temp_arr.append(dist(temp_cluster_3, cl5))
        m_temp_arr.append(dist(temp_cluster_4, cl5))
        m_temp_arr.append(dist(temp_cluster_5, cl5))
        return [min(m_temp_arr), max(m_temp_arr)]
    lower_pointa1 = sorted(clusster_a[0], key = lambda x: x[1])[0]
    lower_pointa2 = sorted(clusster_a[1], key = lambda x: x[1])[0]
    lower_pointa3 = sorted(clusster_a[2], key = lambda x: x[1])[0]
    lower_pointb1 = sorted(clusster_b[0], key = lambda x: x[1])[0]
    lower_pointb2 = sorted(clusster_b[1], key = lambda x: x[1])[0]
    lower_pointb3 = sorted(clusster_b[2], key = lambda x: x[1])[0]
    lower_pointb4 = sorted(clusster_b[3], key = lambda x: x[1])[0]
    lower_pointb5 = sorted(clusster_b[4], key = lambda x: x[1])[0]
    def lower_point(temp_cluster_1, temp_cluster_2):
        m_temp_arr = []
        for temp_points in temp_cluster_2:
            if temp_points != temp_cluster_1:
                summa = dist(temp_cluster_1, temp_points)
                m_temp_arr.append([summa, temp_points])

        return min(m_temp_arr)[1]
    lower_point_a1 = lower_point(lower_pointa1, clusster_a[0])
    lower_point_a2 = lower_point(lower_pointa2, clusster_a[1])
    lower_point_a3 = lower_point(lower_pointa3, clusster_a[2])
    lower_point_b1 = lower_point(lower_pointb1, clusster_b[0])
    lower_point_b2 = lower_point(lower_pointb2, clusster_b[1])
    lower_point_b3 = lower_point(lower_pointb3, clusster_b[2])
    lower_point_b4 = lower_point(lower_pointb4, clusster_b[3])
    lower_point_b5 = lower_point(lower_pointb5, clusster_b[4])
    centr_point_a1 = centr(clusster_a[0])
    centr_point_a2 = centr(clusster_a[1])
    centr_point_a3 = centr(clusster_a[2])
    centr_point_b1 = centr(clusster_b[0])
    centr_point_b2 = centr(clusster_b[1])
    centr_point_b3 = centr(clusster_b[2])
    centr_point_b4 = centr(clusster_b[3])
    centr_point_b5 = centr(clusster_b[4])
    antycentr_point_a1 = antycentr(clusster_a[0])
    antycentr_point_a2 = antycentr(clusster_a[1])
    antycentr_point_a3 = antycentr(clusster_a[2])
    antycentr_point_b1 = antycentr(clusster_b[0])
    antycentr_point_b2 = antycentr(clusster_b[1])
    antycentr_point_b3 = antycentr(clusster_b[2])
    antycentr_point_b4 = antycentr(clusster_b[3])
    antycentr_point_b5 = antycentr(clusster_b[4])
    magic_point_a1 = magic(clusster_a[0], clusster_a[1], clusster_a[2])
    magic_point_a2 = magic(clusster_a[1], clusster_a[2], clusster_a[0])
    magic_point_a3 = magic(clusster_a[2], clusster_a[1], clusster_a[0])
    magic_point_b1 = magicb(clusster_b[0], clusster_b[1], clusster_b[2], clusster_b[3], clusster_b[4])
    magic_point_b2 = magicb(clusster_b[1], clusster_b[0], clusster_b[2], clusster_b[3], clusster_b[4])
    magic_point_b3 = magicb(clusster_b[2], clusster_b[1], clusster_b[0], clusster_b[3], clusster_b[4])
    magic_point_b4 = magicb(clusster_b[3], clusster_b[1], clusster_b[2], clusster_b[0], clusster_b[4])
    magic_point_b5 = magicb(clusster_b[4], clusster_b[1], clusster_b[2], clusster_b[3], clusster_b[0])
    min_magic_dist_a = mindist_a(magic_point_a1, magic_point_a2, magic_point_a3)[0]
    max_magic_dist_a = mindist_a(magic_point_a1, magic_point_a2, magic_point_a3)[1]
    min_magic_dist_b = mindist_b(magic_point_b1, magic_point_b2, magic_point_b3, magic_point_b4, magic_point_b5)[0]
    max_magic_dist_b = mindist_b(magic_point_b1, magic_point_b2, magic_point_b3, magic_point_b4, magic_point_b5)[1]
    def antimag(temp_cluster_1, *points):
        m_temp_arr = []
        data = [point_cl for point_cl in points if point_cl != 0]
        for temp_points in data:
            summa = sum([dist(temp_points, temp_points_num2) for temp_points_num2 in temp_cluster_1])
            m_temp_arr.append([summa, temp_points])
        return max(m_temp_arr)[1]
    cla1_antimag = antimag(clusster_a[0], antycentr_point_a2, antycentr_point_a3)
    cla2_antimag = antimag(clusster_a[1], antycentr_point_a1, antycentr_point_a3)
    cla3_antimag = antimag(clusster_a[2], antycentr_point_a1, antycentr_point_a2)
    clb1_antimag = antimag(clusster_b[0], antycentr_point_b2, antycentr_point_b3, antycentr_point_b4, antycentr_point_b5)
    clb2_antimag = antimag(clusster_b[1], antycentr_point_b1, antycentr_point_b3, antycentr_point_b4, antycentr_point_b5)
    clb3_antimag = antimag(clusster_b[2], antycentr_point_b2, antycentr_point_b1, antycentr_point_b4, antycentr_point_b5)
    clb4_antimag = antimag(clusster_b[3], antycentr_point_b2, antycentr_point_b3, antycentr_point_b1, antycentr_point_b5)
    clb5_antimag = antimag(clusster_b[4], antycentr_point_b2, antycentr_point_b3, antycentr_point_b4, antycentr_point_b1)
    obsysa_centr_a = (centr_point_a1[0] + centr_point_a2[0] + centr_point_a3[0]) / 3
    ordinata_centr_a = (centr_point_a1[1] + centr_point_a2[1] + centr_point_a3[1]) / 3
    obsysa_centr_b = (centr_point_b1[0] + centr_point_b2[0] + centr_point_b3[0] + centr_point_b4[0] + centr_point_b5[0]) / 5
    ordinata_centr_b = (centr_point_b1[1] + centr_point_b2[1] + centr_point_b3[1] + centr_point_b4[1] + centr_point_b5[1]) / 5
    lower_point_final_a_obs = (lower_point_a1[0] + lower_point_a2[0] + lower_point_a3[0]) / 3
    lower_point_final_a_ord = (lower_point_a1[1] + lower_point_a2[1] + lower_point_a3[1]) / 3
    lower_point_final_b_obs = (lower_point_b1[0] + lower_point_b2[0] + lower_point_b3[0] + lower_point_b4[0] + lower_point_b5[0]) / 5
    lower_point_final_b_ord = (lower_point_b1[1] + lower_point_b2[1] + lower_point_b3[1] + lower_point_b4[1] + lower_point_b5[1]) / 5
    # magic_point_final_a1 = (magic_point_a1[0] + magic_point_a2[0] + magic_point_a3[0]) / 3
    # magic_point_final_a2 = (magic_point_a1[1] + magic_point_a2[1] + magic_point_a3[1]) / 3
    # magic_point_final_b1 = (magic_point_b1[0] + magic_point_b2[0] + magic_point_b3[0] + magic_point_b4[0] + magic_point_b5[0]) / 5
    # magic_point_final_b2 = (magic_point_b1[1] + magic_point_b2[1] + magic_point_b3[1] + magic_point_b4[1] + magic_point_b5[1]) / 5
    magic_antycenter_a1 = (cla1_antimag[0] + cla2_antimag[0] + cla3_antimag[0]) / 3
    magic_antycenter_a2 = (cla1_antimag[1] + cla2_antimag[1] + cla3_antimag[1]) / 3
    magic_antycenter_b1 = (clb1_antimag[0] + clb2_antimag[0] + clb3_antimag[0] + clb4_antimag[0] + clb5_antimag[0]) / 5
    magic_antycenter_b2 = (clb1_antimag[1] + clb2_antimag[1] + clb3_antimag[1] + clb4_antimag[1] + clb5_antimag[1]) / 5
    print(int(abs((obsysa_centr_a + ordinata_centr_a + obsysa_centr_b + ordinata_centr_b) * 1_000_0000)))
    print(int(abs((lower_point_final_a_obs + lower_point_final_a_ord + lower_point_final_b_obs + lower_point_final_b_ord) * 1_000_0000)))
    print(int((min_magic_dist_a + max_magic_dist_a) *500_0000) + int((min_magic_dist_b + max_magic_dist_b) *500_0000))
    # print(int(abs((magic_point_final_a1 + magic_point_final_a2 + magic_point_final_b1 + magic_point_final_b2) * 1_000_000)))
    print(int(abs((magic_antycenter_a1 + magic_antycenter_a2 + magic_antycenter_b1 + magic_antycenter_b2) * 1_000_0000)))
    answer1 = int(abs((obsysa_centr_a + ordinata_centr_a + obsysa_centr_b + ordinata_centr_b) * 1_000_0000))
    answer2 = int(abs((lower_point_final_a_obs + lower_point_final_a_ord + lower_point_final_b_obs + lower_point_final_b_ord) * 1_000_0000))
    answer3 = int((min_magic_dist_a + max_magic_dist_a) *500_0000) + int((min_magic_dist_b + max_magic_dist_b) *500_0000)
    answer4 = int(abs((magic_antycenter_a1 + magic_antycenter_a2 + magic_antycenter_b1 + magic_antycenter_b2) * 1_000_0000))
    def get_primes(num):
        a = []
        b = 2
        while b * b <= num:
            if num % b == 0:
                a.append(b)
                num //= b
            else:
                b += 1
        if num > 1:
            a.append(num)
        return a
    kollector = 0
    for integer_scetchik in range(answer1, answer2, -1):
        if kollector == 2:
            break
        n = get_primes(integer_scetchik)
        if len(set(n)) == 3:
            n.sort()
            print(integer_scetchik, n[1])
            kollector += 1
    сounter = 0
    for integer_scetchik in range(answer4, answer3, -1):
        if сounter == 2:
            break
        n = get_primes(integer_scetchik)
        if len(set(n)) == 3:
            n.sort()
            print(integer_scetchik, n[1])
            сounter += 1
    f = {}
    g = {}
    for n in range(1, 50_000):
        if n < 28:
            g[n] = 3 * n - 4
        elif n >= 28:
            g[n] = g[n - 5] - 15
    for n in range(50_000, 0, -1):
        if n >= 31054:
            f[n] = 3 * (g[n - 2] - 15)
        elif n < 31054:
            f[n] = f[n + 4] + 3020
        print(f[34700])







# k = 0

def start():

    # if k > 0:

    #     os.system('cls')
    
    # k += 1

    start_print()

    print('Enter command:\n')

    command = input()

    if command == 'remove_symb':

        print('\nEnter dir:\n')

        dir = "".join(input())

        fille = open(dir)
        
        print('What remove?\n')
        
        remover = input

        fille.remove(remover)

        time.sleep(2)

        print('done')

        start()
    
    elif command == 'Cheat code: zvargon_vilit':

        start_print()

        st_command = input()

        if st_command == 'schet':

            for x in range(1, 1000):
                for y in range(1, 1000):
                    for w in range(1, 1000):
                        print(x + y + w + x + y + w + x + y + w, x * y * w * x + y + w, x - y - w - x - y - w)
                        end_wrong()
        
        elif st_command == 'number_27':

            number_27_ege_podscet()
        
        elif st_command == 'swaper':

            print('\nEnter fiile name:\n')

            dirs = input()

            with open(dirs, 'r+', encoding = 'utf-8') as fiile:

                fiile.seek(0)

                spisok = [x for x in fiile.read().split()]

                random.shuffle(spisok)

                writewnd = " ".join(spisok)

                fiile.seek(0)

                fiile.write(writewnd)

        elif st_command == 'killer':

            print('\nEnter fiile name:\n')

            dirs = input()

            with open(dirs, 'r+', encoding = 'utf-8') as fiile:

                fiile.seek(0)

                spisok = [x for x in fiile.read().split()]

                random.shuffle(spisok)

                writewnd = " ".join(spisok)

                writer = writewnd

                random.shuffle(spisok)

                writewnd = " ".join(spisok)

                writer += writewnd

                fiile.write(writewnd)

    elif command == 'die':

        s = [x ** x ** x for x in range(10)]
    
    elif command == 'schet':

        for x in range(1, 1000):
            for y in range(1, 1000):
                for w in range(1, 1000):
                    print(x + y + w + x + y + w + x + y + w, x * y * w * x + y + w, x - y - w - x - y - w)

    elif command == 'create':
        
        print('\nEnter full name and dir of fiile:\n')

        name_fiile = input()

        try:

            with open(name_fiile, 'x', encoding='utf-8') as fiile:

                fiile.write('|               BY Anigilator :)               |')

                print('\nCreated\n')
                
                time.sleep(5)

                start()

        except FileExistsError:

            print('Issue')

            start()

    elif command == 'exit':
        
        os.system('cls')

        print('\nBye!\n')

        time.sleep(3)

        exit()

    else:

        print('\nCry lol\n')

        end_wrong()

        exit()
    






start()