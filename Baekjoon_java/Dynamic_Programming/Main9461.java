package com.company;

import java.io.*;

public class Main9461 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i=0; i<t; i++) {
            int n = Integer.parseInt(br.readLine());

            if (n<=3) System.out.println(1);
            else {
                long[] arr = new long[n+1];
                arr[1] = 1;
                arr[2] = 1;
                arr[3] = 1;

                for (int j=4; j<=n; j++) {
                    arr[j] = arr[j-3] + arr[j-2];
                }
                System.out.println(arr[n]);
            }
        }
        br.close();
    }
}
