class Solution:
    pascalRows = [[1],[1,1]]
    def getRow(self, rowIndex: int) -> List[int]:
        while(rowIndex >= len(self.pascalRows)):
            lastRow = self.pascalRows[-1]
            newRow = [1]
            for i in range(0, len(lastRow) - 1):
                newRow.append(lastRow[i] + lastRow[i+1])
            newRow.append(1)
            self.pascalRows.append(newRow)
        self.pascalRows.pop(0)
        return self.pascalRows[-1]