from flask import Flask, render_template, request
from math import comb

app = Flask(__name__)

# Function to calculate binomial probability
def binomial_probability(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Function to calculate cumulative binomial probability
def cumulative_binomial_probability(n, k, p):
    probabilities = [binomial_probability(n, i, p) for i in range(k + 1)]
    return sum(probabilities), probabilities

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        n = int(request.form['n'])
        k = int(request.form['k'])
        p = float(request.form['p'])

        if n < 0 or k < 0 or k > n or not (0 <= p <= 1):
            raise ValueError("Invalid input values.")

        # Step-by-step calculations
        steps = []

        # Step 1: PMF Formula
        steps.append("Langkah 1: Memahami Fungsi Massa Probabilitas Binomial (PMF)")
        steps.append(r"Probabilitas untuk mendapatkan tepat \( k \) keberhasilan dari \( n \) percobaan dihitung dengan rumus:")
        steps.append(r"\[ P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \]")

        # Step 2: Identify Values
        steps.append("Langkah 2: Identifikasi Nilai yang Diberikan")
        steps.append(f"Jumlah percobaan (n) = {n}, Probabilitas keberhasilan (p) = {p}, Jumlah keberhasilan (k) = {k}")

        # Step 3: Substitution
        steps.append("Langkah 3: Substitusi Nilai ke dalam Rumus")
        steps.append(rf"\[ P(X = {k}) = \binom{{{n}}}{{{k}}} ({p})^{k} (1-{p})^{{{n-k}}} \]")

        # Step 4: Coefficient
        coefficient = comb(n, k)
        steps.append("Langkah 4: Hitung Koefisien Binomial")
        steps.append(rf"\[ \binom{{{n}}}{{{k}}} = {coefficient} \]")

        # Step 5: Calculate PMF
        pmf = binomial_probability(n, k, p)
        steps.append("Langkah 5: Hitung Probabilitas")
        steps.append(rf"\[ P(X = {k}) = {coefficient} \cdot ({p})^{k} \cdot (1-{p})^{{{n-k}}} = {pmf} \]")

        # Step 6: CDF Formula
        steps.append("Langkah 6: Memahami Fungsi Distribusi Kumulatif Binomial (CDF)")
        steps.append("Probabilitas kumulatif untuk mendapatkan hingga \( k \) keberhasilan dihitung dengan rumus:")
        steps.append(r"\[ P(X \leq k) = \sum_{i=0}^{k} \binom{n}{i} p^i (1-p)^{n-i} \]")

        # Step 7: CDF Calculation
        cumulative_probability, probabilities = cumulative_binomial_probability(n, k, p)
        steps.append("Langkah 7: Hitung Probabilitas Kumulatif")
        for i, prob in enumerate(probabilities):
            steps.append(rf"\[ P(X = {i}) = {prob} \]")

        # Step 8: Final CDF
        steps.append("Langkah 8: Jumlahkan Semua Term")
        steps.append(rf"\[ P(X \leq {k}) = {cumulative_probability} \]")

        return render_template('index.html', steps=steps, pmf=pmf, cdf=cumulative_probability, n=n, k=k, p=p)

    except ValueError as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
