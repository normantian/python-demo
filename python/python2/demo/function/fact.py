'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
'''
#�׳�
'''
ʹ�õݹ麯�����ŵ����߼���������ȱ���ǹ���ĵ��ûᵼ��ջ�����

���β�ݹ��Ż������Կ���ͨ��β�ݹ��ֹջ�����
β�ݹ���ʵ�Ϻ�ѭ���ǵȼ۵ģ�û��ѭ�����ı������ֻ��ͨ��β�ݹ�ʵ��ѭ����

Python��׼�Ľ�����û�����β�ݹ����Ż����κεݹ麯��������ջ��������⡣

β�ݹ����ʱ����������Ż���ջ��������.
��ˣ����۶��ٴε���Ҳ���ᵼ��ջ�����

�ź����ǣ�������������û�����β�ݹ����Ż���Python������Ҳû�����Ż�.
���ԣ���ʹ�������fact(n)�����ĳ�β�ݹ鷽ʽ��Ҳ�ᵼ��ջ�����
'''
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


#�����Python����Ա
def fact(x):
    return x>1 and x * fact(x-1) or 1

#������Python����Ա
f = lambda x: x and x * f(x - 1) or 1
print f(6)

#Python ר��
facter = lambda x : reduce(int.__mul__, xrange(2,x+1),1)
print facter(4)

#ר�Ҽ�����Ա
import cmath
print fact(6)


#Python �ڿ�
import sys
#@tailcall
def fact1(x, acc=1):
    if x: return fact1(x.__sub__(1), acc.__mul__(x))
    return acc
sys.stdout.write(str(fact1(6)) + '\n')
