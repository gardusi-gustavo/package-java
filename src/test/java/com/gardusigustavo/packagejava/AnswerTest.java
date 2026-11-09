package com.gardusigustavo.packagejava;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class AnswerTest {
    @Test
    void answerIs42() {
        assertEquals(42, Answer.value());
    }
}
