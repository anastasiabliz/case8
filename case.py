'''currency exchange chart'''


def first_task():
    import matplotlib.pyplot as plt
    a = []
    b = []
    c = 1
    file = open('text1.txt','r')
    for i in file:
        b.append(c)
        a.append(float(i))
        c += 1
    plt.plot(b, a)
    plt.show()
first_task()





'''multiple currency charts'''


def second_task():
    import matplotlib.pyplot as plt
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d = []
    d0 = 1
    file1 = open('text2.txt', 'r')
    for i in file1:
        s1, s2, s3, s4 = i.split()
        d.append(d0)
        d1.append(float(s1))
        d2.append(float(s2))
        d3.append(float(s3))
        d4.append(float(s4))
        d0 += 1
    plt.plot(d, d1, d, d2, d, d3, d, d4)
    plt.show()
second_task()


'''Finalization of graphs'''

def third_task():
    import matplotlib.pyplot as plt
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d = []
    d0 = 1
    file1 = open('text2.txt', 'r')
    for i in file1:
        s1, s2, s3, s4 = i.split()
        d.append(d0)
        d1.append(float(s1))
        d2.append(float(s2))
        d3.append(float(s3))
        d4.append(float(s4))
        d0 += 1
    plt.plot(d, d1, d, d2, d, d3, d, d4)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
    plt.grid(True)
    plt.show()
third_task()





'''More about graphs'''
def fourth_task():
    import matplotlib.pyplot as plt
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d = []
    d0 = 1
    file1 = open('text2.txt', 'r')
    for i in file1:
        s1, s2, s3, s4 = i.split()
        d.append(d0)
        d1.append(float(s1))
        d2.append(float(s2))
        d3.append(float(s3))
        d4.append(float(s4))
        d0 += 1
        # subplot 1
    plt.subplot(221)
    plt.plot(d, d1)
    plt.title(r'$\sin(x)$')
    plt.grid(True)
        # subplot 2
    plt.subplot(222)
    plt.plot(d, d2, 'g')
    plt.axis('equal')
    plt.grid(True)
    plt.title(r'$\cos(x)$')
        # subplot 3
    plt.subplot(223)
    plt.plot(d, d3, 'ro')
    plt.title(r'$x^2$')
        # subplot 4
    plt.subplot(224)
    plt.plot(d, d4)
    plt.subplot(224).spines['left'].set_position('center')
    plt.subplot(224).spines['bottom'].set_position('center')
    plt.title(r'$x$')
    plt.show()
fourth_task()


''''''


def fifth_task():
    import matplotlib.pyplot as plt
    a = []
    b = []
    c = 1
    file = open('text1.txt', 'r')
    for i in file:
        b.append(c)
        a.append(float(i))
        c += 1
    plt.subplot(111, polar=True)
    plt.plot(b, a, lw=2)
    plt.show()

fifth_task()

def sixth_task():
    import matplotlib.pyplot as plt
    a = []
    b = []
    c = 1
    file = open('text1.txt', 'r')
    for i in file:
        b.append(c)
        a.append(float(i))
        c += 1
    plt.plot(b, a, lw=3)
    plt.axis('equal')
    plt.show()
sixth_task()


def eight_task():
    import matplotlib.pyplot as plt
    a = []
    b = []
    c = 1
    file = open('text1.txt', 'r')
    for i in file:
        b.append(c)
        a.append(float(i))
        c += 1
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .030, r'$\mu=100,\ \sigma=15$')
    plt.text(50, .033,
             r'$\varphi_{\mu,\sigma^2}(x) = \frac{1}{\sigma\sqrt{2\pi}} \,e^{ -\frac{(x- \mu)^2}{2\sigma^2}} = \frac{1}{\sigma} \varphi\left(\frac{x - \mu}{\sigma}\right),\quad x\in\mathbb{R}$',
             fontsize=20, color='red')
    plt.axis([40, 160, 0, 0.04])
    plt.grid(True)
    plt.show()
eight_task()














