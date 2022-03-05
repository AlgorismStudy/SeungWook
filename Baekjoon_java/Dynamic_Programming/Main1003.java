package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1003 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i=0; i<T; i++) {
            int N = Integer.parseInt(br.readLine());
            System.out.println(fibo(N) + " " + fibo(N+1));
        }
        br.close();
    }

    public static int fibo(int N) {
        int fibo0 = 1;
        int fibo1 = 0;
        int fibo2 = 1;

        if (N==0) return fibo0;
        else if (N==1) return fibo1;
        else {
            for (int i=0; i<N; i++) {
                fibo0 = fibo1;
                fibo1 = fibo2;
                fibo2 = fibo0 + fibo1;
            }
            return fibo0;
        }
    }
}
