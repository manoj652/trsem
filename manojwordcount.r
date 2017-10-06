
# Load

library(tm)
library(wordcloud)
text <- readLines(file.choose())

# Read the text file from desktop
#filePath <- "C:/Users/SOIS/Desktop/m.txt"
text <- readLines("m.txt")
inspect(docs)

docs <- Corpus(VectorSource(text))
# clean data 
trans <- content_transformer(function (x , pattern ) gsub(pattern, " ", x))

#create the document
dtm <- TermDocumentMatrix(docs)
mat <- as.matrix(dtm)
v <- sort(rowSums(mat),decreasing=TRUE)

#data frame
d <- data.frame(word = names(v),freq=v)
head(d, 10)



