FROM amazoncorretto:17.0.14 AS builder

WORKDIR /app
COPY . .
RUN ./gradlew clean build -x test

###################################

FROM amazoncorretto:17.0.14

WORKDIR /app
COPY --from=builder /app/build/libs/*.jar app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
