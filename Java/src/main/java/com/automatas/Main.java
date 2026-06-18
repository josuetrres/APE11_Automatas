package com.automatas;

import java.io.FileReader;

public class Main {

    public static void main(String[] args) {

        try {

            long inicio = System.nanoTime();

            parser p = new parser(new Lexer(new FileReader("entrada.txt")));

            p.parse();

            long fin = System.nanoTime();

            double tiempoMs = (fin - inicio) / 1_000_000.0;

            System.out.println(
                    "\nTiempo de ejecución: "
                            + tiempoMs
                            + " ms");

        } catch (Exception e) {

            System.err.println(
                    "Error durante el análisis:");

            e.printStackTrace();
        }
    }
}
