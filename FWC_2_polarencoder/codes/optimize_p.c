#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 1024  // Number of bits in the message
#define K 512   // Number of information bits

int main(int argc, char* argv[]) {
  // Allocate memory for the message and encoded message
  int* message = (int*) malloc(N * sizeof(int));
  int* encoded = (int*) malloc(N * sizeof(int));

  // Initialize the message with random bits
  for (int i = 0; i < N; i++) {
    message[i] = rand() % 2;
  }

  // Perform polar encoding on the message
  for (int i = 0; i < K; i++) {
    encoded[i] = message[i];
  }
  for (int i = K; i < N; i++) {
    encoded[i] = 0;
  }
  int num_iterations = (int) ceil(log2(N));
  for (int i = 0; i < num_iterations; i++) {
    int block_size = pow(2, i);
    for (int j = 0; j < N; j += (2 * block_size)) {
      for (int k = 0; k < block_size; k++) {
        int index = j + k;
        encoded[index + block_size] = encoded[index] ^ encoded[index + block_size];
      }
    }
  }

  // Print the encoded message
  for (int i = 0; i < N; i++) {
    printf("%d", encoded[i]);
  }
  printf("\n");

  // Free memory
  free(message);
  free(encoded);

  return 0;
}
