package com.gardusigustavo.packagejava;

public final class AnswerCheck {
    private AnswerCheck() {}

    public static void main(String[] args) {
        if (Answer.value() != 42) {
            throw new AssertionError("Answer.value() != 42");
        }
    }
}
