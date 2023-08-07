class Pagination:
    def __init__(self, items, pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)

        self.currentPage = 1
        self.totalPages = (len(items) + pageSize - 1) // pageSize

    def getVisibleItems(self):
        start_idx = (self.currentPage - 1) * self.pageSize
        end_idx = self.currentPage * self.pageSize
        return self.items[start_idx:end_idx]

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        if pageNum > self.totalPages:
            pageNum = self.totalPages
        elif pageNum < 1:
            pageNum = 1
        self.currentPage = pageNum
        return self


if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")

    p = Pagination(alphabetList, 4)

    print(p.getVisibleItems())
    print(p.nextPage().getVisibleItems())
    print(p.nextPage().nextPage().getVisibleItems())
    print(p.lastPage().getVisibleItems())
