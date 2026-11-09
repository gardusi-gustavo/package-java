# package-java

Java/JVM reference package: a small library, a Spring Boot example, tests, and
release notes. It is the “how do I set up Java here?” repository.

## Layout

| Path | Holds |
| --- | --- |
| `src/main/java/` | publishable library |
| `src/test/java/` | JUnit tests |
| `examples/spring-boot-app/` | full Spring Boot demo |
| `docs/` | usage and release notes |

## Build

```bash
mvn -q test
```
