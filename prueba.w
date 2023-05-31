var float A, B, C, D, E, F, G, H, I, J, K;

main {
    A = B + C * (D - E / F) * H;
    B = E - F;
    while (A * B - C >= D * E / (G + H)) {
        H = J * K + B;
        if (B < H){
            B = H + J;
            while (B > A + C){
                write(A + B * C + D - E);
                B = B - J; 
            }
        }
        else{
            while(A - D < C + B){
                A = A + B;
                write(B - D);
            }
        }
    }
    F = A + B;
}

end