### NiNumerical
---
##### Numerical method samples in python & pyplot. Refer to **<<Numerical Methods for Engineers 7th>>**.
> pip install -r requirements.txt

to install dependencies.

---
- RootFinding
  - Bracketing (simple)
    - Bisection Method
    - False Position Method
  - Open (faster, but may diverge or cycle)
    - Fixed Point Iteration
    - Newton-Raphson Method (needs f and f') $ x_i+1 = x_i + f(x_i)/f'(x_i) $
      - Important Points: Newton’s method is useful in cases of large values of f’(x) i.e. when the graph of f(x) while crossing the x-axis is nearly vertical. May converge slowly.
      - It is not preferred when the graph of f(x) is nearly horizontal where it crosses the x-axis as the values of f’(x) have negative values in this case.
      - It is sensitive to starting value.
      - Convergence fails if the starting point is nor near the root.
      - The formula converges provided the initial approximation x0 is chosen sufficiently close to the root.
      - **It is generally used to improve the result obtained by the other methods.** 
      - It has quadratic convergence i.e. order of convergence is 2. The subsequent error at each step is proportional to the square of the error at the previous step.
    - Modified Newton-Raphson Method $ x_i+1 = x_i + f(x_i)f'(x_i) / ( [f'(x_i)]^2 -f(x_i)f''(x_i) ) $
    - Secant Method (needs 2 points) $ x_i+1 = x_i + u(x_i)/u(x_i) $
    - Modified Secant Method $ x_i+1 = x_i - u(x_i)(x_i-1 + x_i)/(u(x_i-1) - u(x_i)) $
    - Inverse Quadratic Interpolation (needs 3 points)
  - Graphical (for debug)
- LinearAlgebra
- CurveFitting
- Differentiation
- Integration
- Optimization
  - Convex
  - Nonlinear
  - more
- ODE
- PDE


Sources of Error
---
- Modeling Error
  - Formulation Error
  - Data Uncertainty
  - *Blunders
- Numerical Error
  - Truncation Error
    - Taylor Series
  - Roundoff Error
    - Quantization Error
    - Numerical Manipulations
      - Adding large and small numbers
      - Subtractive cancellation
