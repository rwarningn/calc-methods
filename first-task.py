import math

def f(x):
    return 4 * math.cos(x) + 0.3 * x

def df(x):
    return -4 * math.sin(x) + 0.3

def print_header():
    print("=" * 80)
    print("Function: f(x) = 4cos(x) + 0.3x")
    print("Segment: [A, B] = [-15; 5]")
    print("Accuracy: epsilon = 10^(-5)")
    print("=" * 80)
    print()

def separate_roots(A, B, N):
    intervals = []
    h = (B - A) / N
    start = A
    
    for i in range(N):
        end = start + h
        
        if f(end) * f(start) < 0:
            intervals.append((start, end))
        elif f(end) == 0:
            intervals.append((end, end))
        elif i == 0 and f(start) == 0:
            intervals.append((start, start))
        
        start = end
    
    return intervals

def bisect_method(A, B, eps):
    start, end = A, B
    x = start
    iter_count = 0
    
    print("=" * 60)
    print(f"Initial segment: [{A:.10f}; {B:.10f}]")
    
    while end - start > eps:
        iter_count += 1
        x = (start + end) / 2
        
        f_start, f_x, f_end = f(start), f(x), f(end)
        
        if (f_start * f_x < 0 and f_x * f_end < 0) or \
           (f_start * f_x > 0 and f_x * f_end > 0):
            print("Error: root of even multiplicity")
            return
        
        if f_start * f_x < 0:
            end = x
        elif f_end * f_x < 0:
            start = x
        else:
            break
    
    print(f"Steps: {iter_count}")
    print(f"Approximate solution x_m: {x:.15f}")
    print(f"Length of the last segment |x_m - x_(m-1)|: {end - start:.15e}")
    print(f"Residual |f(x_m)|: {abs(f(x)):.15e}")
    print()

def newton_method(A, B, eps, max_iter, df_eps):
    x = (A + B) / 2
    x0 = x
    iter_count = 0
    
    print("=" * 60)
    print(f"Initial approximation: x_0 = {x:.10f}")
    
    while (abs(x - x0) > eps or iter_count == 0) and iter_count < max_iter:
        iter_count += 1
        x0 = x
        
        df_x0 = df(x0)
        if abs(df_x0) < df_eps:
            print(f"Error: derivative too small |df(x_0)| = {abs(df_x0):.2e} on step {iter_count}")
            return
        
        x = x0 - f(x0) / df_x0
    
    if abs(x - x0) > eps:
        print(f"The maximum number of iterations has been reached: {max_iter}")
        print(f"Approximate solution x_m: {x:.15f}")
        print(f"Last modified |x_m - x_(m-1)|: {abs(x - x0):.15e}")
        print(f"Residual |f(x_m)|: {abs(f(x)):.15e}")
        print()
        return
    
    print(f"Steps: {iter_count}")
    print(f"Approximate solution x_m: {x:.15f}")
    print(f"Last modified |x_m - x_(m-1)|: {abs(x - x0):.15e}")
    print(f"Residual |f(x_m)|: {abs(f(x)):.15e}")
    print()

def modified_newton_method(A, B, eps, max_iter, df_eps, m):
    x = (A + B) / 2
    x0 = x
    iter_count = 0
    
    print("=" * 60)
    print(f"Initial approximation: x_0 = {x:.10f}")
    print(f"Root multiplicity m = {m}")
    
    while (abs(x - x0) > eps or iter_count == 0) and iter_count < max_iter:
        iter_count += 1
        x0 = x
        
        df_x0 = df(x0)
        if abs(df_x0) < df_eps:
            print(f"Error: derivative too small |df(x_0)| = {abs(df_x0):.2e} on step {iter_count}")
            return
        
        x = x0 - m * f(x0) / df_x0
    
    if abs(x - x0) > eps:
        print(f"The maximum number of iterations has been reached: {max_iter}")
        print(f"Approximate solution x_m: {x:.15f}")
        print(f"Last modified |x_m - x_(m-1)|: {abs(x - x0):.15e}")
        print(f"Residual |f(x_m)|: {abs(f(x)):.15e}")
        print()
        return
    
    print(f"Steps: {iter_count}")
    print(f"Approximate solution x_m: {x:.15f}")
    print(f"Last modified |x_m - x_(m-1)|: {abs(x - x0):.15e}")
    print(f"Residual |f(x_m)|: {abs(f(x)):.15e}")
    print()

def secant_method(A, B, eps, max_iter, df_eps):
    x0, x1 = A, B
    x2 = 0
    iter_count = 0
    
    print("=" * 60)
    print(f"Initial approximation: x_0 = {x0:.10f}, x_1 = {x1:.10f}")
    
    for i in range(1, max_iter + 1):
        f0, f1 = f(x0), f(x1)
        
        if abs(f1 - f0) < df_eps:
            print(f"Error: |f(x_1) - f(x_0)| too small = {abs(f1 - f0):.2e}")
            return
        
        x2 = x1 - f1 / (f1 - f0) * (x1 - x0)
        
        if abs(x2 - x1) < eps:
            iter_count = i
            break
        
        x0, x1 = x1, x2
    
    if iter_count == 0:
        print(f"The maximum number of iterations has been reached: {max_iter}")
        print(f"Approximate solution x_m: {x2:.15f}")
        print(f"Last modified |x_m - x_(m-1)|: {abs(x2 - x1):.15e}")
        print(f"Residual |f(x_m)|: {abs(f(x2)):.15e}")
        print()
        return
    
    print(f"Steps: {iter_count}")
    print(f"Approximate solution x_m: {x2:.15f}")
    print(f"Last modified |x_m - x_(m-1)|: {abs(x2 - x1):.15e}")
    print(f"Residual |f(x_m)|: {abs(f(x2)):.15e}")
    print()

def main():
    A = -15.0
    B = 5.0
    eps = 1e-5
    
    print_header()
    
    print("№1. Root separation")
    print("-" * 80)
    
    s = "yes"
    intervals = []
    
    while s.lower() != "no":
        try:
            N = int(input("Enter N (the number of segment partitions): "))
            if N < 2:
                print("N must be >= 2")
                continue
                
            intervals = separate_roots(A, B, N)
            h = (B - A) / N
            
            print(f"\nPartition step h = {h:.10f}")
            print(f"Segments of sign change found: {len(intervals)}\n")
            
            for idx, interval in enumerate(intervals, 1):
                print(f"Segment {idx}: [{interval[0]:.10f}; {interval[1]:.10f}]")
            
            print()
            s = input("Do we need a new N? (yes/no): ")
        except ValueError:
            print("Input error! Please enter an integer.")
    
    if not intervals:
        print("Roots not found!")
        return
    
    print("\n" + "=" * 80)
    print("№2. Clarification of roots")
    print("=" * 80)
    print()
    
    newton_max_iter = 200
    secant_max_iter = 300
    df_eps = 1e-15
    m = 1 
    
    for idx, interval in enumerate(intervals, 1):
        print("\n" + "#" * 80)
        print(f"Root №{idx}: Segment [{interval[0]:.10f}; {interval[1]:.10f}]")
        print("#" * 80)
        print()
        
        bisect_method(interval[0], interval[1], eps)
        newton_method(interval[0], interval[1], eps, newton_max_iter, df_eps)
        modified_newton_method(interval[0], interval[1], eps, newton_max_iter, df_eps, m)
        secant_method(interval[0], interval[1], eps, secant_max_iter, df_eps)
    
    print("\n" + "=" * 80)
    print("solution completed")
    print("=" * 80)

if __name__ == "__main__":
    main()