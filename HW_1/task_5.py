# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
print("x1 = ") 
x1 = float(input())
print("y1 = ") 
y1 = float(input())
print("x2 = ") 
x2 = float(input())
print("y2 = ") 
y2 = float(input())
import math
dist = math.sqrt(((x2 - x1) ** 2 + (y2 - y1) ** 2))

print("Расстояние =", round(dist, 2))