import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.pyplot as plt
 
def drawDiagram(a_low, a_high, a, b, c):
    alpha_np = np.linspace(a_low, a_high, 10000)

    a_steady = []
    a_unsteady = []
    root_steady = []
    root_unsteady = []

    for alpha in alpha_np :
        coefficients = [a, b, alpha+c]
        roots = np.roots(coefficients)
        roots = roots.tolist()

        if roots[0].imag == 0 and roots[1].imag == 0:
            root_steady.append(roots)
            a_steady.append(alpha)       
        else: 
            root_unsteady.append(roots)
            a_unsteady.append(alpha)
        
    root_steady = np.array(root_steady)
    root_unsteady = np.array(root_unsteady, dtype=complex)

    return a_steady, a_unsteady, root_steady, root_unsteady


# # dx = a - x^2
a_steady, a_unsteady, root_steady, root_unsteady = drawDiagram(-1, 1, -1, 0, 0)
plt.plot(a_steady,root_steady[:,0],label = "steady state", color = 'b')
plt.plot(a_steady,root_steady[:,1], color = 'b')
plt.plot(a_unsteady,root_unsteady[:,0],color = 'r',label = "no steady state", linestyle="--")
plt.plot(a_unsteady,root_unsteady[:,1],color = 'r',linestyle="--")
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$x_0 (\alpha)$')
plt.legend()
plt.title(r'$ \dot{x} = \alpha - x^2$' )
plt.show()

# dx = a - 2x^2 - 3
a_steady, a_unsteady, root_steady, root_unsteady = drawDiagram(-1, 3, -2, 0, -3)
plt.plot(a_steady,root_steady[:,0],label = "steady state", color = 'b')
plt.plot(a_steady,root_steady[:,1], color = 'b')
plt.plot(a_unsteady,root_unsteady[:,0],color = 'r',label = "no steady state", linestyle="--")
plt.plot(a_unsteady,root_unsteady[:,1],color = 'r',linestyle="--")
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$x_0 (\alpha)$')
plt.legend()
plt.title(r'Bifurcation diagramm, $ \dot{x} = \alpha - 2x^2 -3$')
plt.show()


# alpha = -1
X = np.linspace(-10,10,100)
fig = plt.figure()
gs = gridspec.GridSpec(nrows=1, ncols=2)

ax1 = fig.add_subplot(gs[0,0])
Y1 = -X**2 - 1
ax1.plot(Y1,X)
ax1.set_title(r'$ \dot{x} = \alpha - x^2$, $\alpha$ = -1')

ax2 = fig.add_subplot(gs[0,1])
Y2 = -2 * X**2 - 4
ax2.plot(Y2,X)
ax2.set_title(r'$ \dot{x} = \alpha - 2x^2-3$, $\alpha$ = -1')
plt.show()