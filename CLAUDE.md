# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Gradle-based project that generates Protocol Buffer stubs for the lemon-pi racing telemetry system. The project uses Protocol Buffers v3.25.3 and gRPC v1.57.0 to define communication protocols between race cars and pit crews.

## Key Architecture

The project defines several gRPC services:
- **CommsService** (`lemon-pi.proto`): Core communication between cars and pits, handling real-time messaging, telemetry, and race status updates
- **CarDataService** (`car-data.proto`): Public API for retrieving car position, telemetry, and race field data
- **AdminService** (`meringue-admin.proto`): Administrative functions for managing race connections and car associations
- **PitcrewService** (`pitcrew.proto`): Functions for a pit crew to observe their cars

Message types include:
- Car telemetry (coolant temp, fuel levels, lap times)
- Race position and status updates
- GPS positioning data
- Driver messaging
- Pit entry/exit notifications

## Essential Commands

```bash
# Build the project and generate Protocol Buffer stubs
./gradlew build

# Generate only the protobuf files without running tests
./gradlew generateProto

# Clean build artifacts
./gradlew clean

# Assemble JAR without tests
./gradlew assemble
```

## Code Generation

The project uses the `com.google.protobuf` Gradle plugin to generate:
- Java Protocol Buffer classes
- gRPC service stubs (Java and Kotlin)
- Python stubs (found in `generated/` directory)

Generated files are placed in `build/generated/source/proto/` and should not be manually edited.

## Dependencies

- Kotlin 1.8.22 with Java 11 compatibility
- Protocol Buffers 3.25.3
- gRPC 1.57.0 (locked version to match lemon-pi main project)
- Kotlin coroutines for async operations