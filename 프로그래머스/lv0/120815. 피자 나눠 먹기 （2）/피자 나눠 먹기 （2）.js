function solution(n) {
    const gcd = (a, b) => a % b === 0 ? b : gcd(b, a % b);
    return answer =n/gcd(n,6)

}