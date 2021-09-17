/**
 * Sudoku Solution Validator by Stilian Balasopoulov
 * CS3600(a)
 */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <pthread.h>
#define NUM_THREADS 27
#define pass (void) 0

int valid[NUM_THREADS] = {0};
int sudoku[9][9];

typedef struct {
	int row;
	int column;
} parameters;

// Checks if 3x3 grid in sudoku[][] contains only numbers 1-9
void *gridValid (void* param) {
	parameters *params = (parameters *) param;
	int row = params->row;
	int col = params->column;
	int validArray[9] = {0}, i, j;

	// Verifying parameters conform to 3x3 grid
	if (row > 6 || row % 3 != 0 || col > 6 || col % 3 != 0) {
		printf("Invalid row or column. row = %d col = %d", row, col);
		pthread_exit(NULL);
	}

	// Verifying each number contains only numbers 1-9
	for (i = row; i < row + 3; i++) {
		for (j = col; j < col + 3; j++) {
			int num = sudoku[i][j];
			if (num < 1 || num > 9 || validArray[num - 1] == 1)
				pthread_exit(NULL);
			else validArray[num - 1] = 1;
		}
	}
	// Inputs validation into boolean array
	valid[row + col / 3] = 1;
	pthread_exit(NULL);
}

// Checks if column contains only numbers 1-9
void *columnValid (void* param) {
	parameters *params = (parameters *) param;
	int row = params->row;
	int col = params->column;
	int validArray[9] = {0}, i;

	// Verifying parameters conform to a column
	if (row != 0 || col > 8) {
		printf("Invalid row or column. row = %d col = %d", row, col);
		pthread_exit(NULL);
	}

	// Verifying each number in column is between 1-9
	for (i = 0; i < 9; i++) {
		int num = sudoku[i][col];
		if (num < 1 || num > 9 || validArray[num - 1] == 1)
			pthread_exit(NULL);
		else validArray[num - 1] = 1;
	}

	// Inputs validation into boolean array
	valid[18 + col] = 1;
	pthread_exit(NULL);
}

// Checks if row contains only numbers 1-9
void *rowValid (void* param) {
	parameters *params = (parameters *) param;
	int row = params->row;
	int col = params->column;
	int validArray[9] = {0}, i;

	// Verifying parameters conform to a column
	if (col != 0 || row > 8) {
		printf("Invalid row or column. row = %d col = %d", row, col);
		pthread_exit(NULL);
	}

	// Verifying each number in row is between 1-9
	for (i = 0; i < 9; i++) {
		int num = sudoku[row][i];
		if (num < 1 || num > 9 || validArray[num - 1] == 1)
			pthread_exit(NULL);
		else validArray[num - 1] = 1;
	}

	// Inputs validation into boolean array
	valid[9 + row] = 1;
	pthread_exit(NULL);
}

int main() {
	pthread_t threads[NUM_THREADS];
	int threadsIndex = 0;
	int i,j;

	// I/O for puzzle and output
	FILE *sudokuPuzzle = fopen("SudokuPuzzle.txt", "r");
	FILE *testResults = fopen("testResults.txt", "w");
	if (sudokuPuzzle == NULL || testResults == NULL) {
		printf("ERROR: Could not open txt file.");
		exit(-1);
	}

	// Scanning input file and placing numbers in puzzle
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			char c;
			if (fscanf(sudokuPuzzle, " %c", &c) != 1)
				pass;
			else if (isdigit((unsigned char)c))
				sudoku[i][j] = c - '0';
		}
	}

	// Printing Sudoku Puzzle to testResults.txt
	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++) {
			fprintf(testResults, "%d ", sudoku[i][j]);
		}
		fprintf(testResults, "\n");
	}

	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++) {
			if (i % 3 == 0 && j % 3 == 0) {
				parameters *data = (parameters *) malloc(sizeof(parameters));
				data->row = i;
				data->column = j;
				pthread_create(&threads[threadsIndex++], NULL, gridValid, data);
			}
			if (i == 0) {
				parameters *colData = (parameters *) malloc(sizeof(parameters));
				colData->row = i;
				colData->column = j;
				pthread_create(&threads[threadsIndex++], NULL, columnValid, colData);
			}
			if (j == 0) {
				parameters *rowData = (parameters *) malloc(sizeof(parameters));
				rowData->row = i;
				rowData->column = j;
				pthread_create(&threads[threadsIndex++], NULL, rowValid, rowData);
			}
		}
	}

	// Wait for all threads to finish
	for (i = 0; i < NUM_THREADS; i++) {
		pthread_join(threads[i], NULL);
	}

	fprintf(testResults, "\n");

	for (i = 0; i < NUM_THREADS; i++) {
		if (valid[i] == 0) {
			fprintf(testResults, "Solution is Invalid.");
			return 0;
		}
	}

	fprintf(testResults, "Solution is Valid!");
	return 0;
}
