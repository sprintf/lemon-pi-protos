#!/usr/bin/env bash
# Regenerates the Swift Protocol Buffer + gRPC sources consumed by Package.swift.
#
# Requires on PATH: protoc, protoc-gen-swift (apple/swift-protobuf) and
# protoc-gen-grpc-swift-2 (grpc/grpc-swift-protobuf). Keep the generator
# versions in step with the dependency versions in Package.swift.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PROTO_DIR="$ROOT/src/main/proto"
OUT_DIR="$ROOT/swift/LemonPiProtos"

rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

protoc \
  --proto_path="$PROTO_DIR" \
  --swift_out="$OUT_DIR" \
  --swift_opt=Visibility=Public \
  --grpc-swift-2_out="$OUT_DIR" \
  --grpc-swift-2_opt=Visibility=Public \
  "$PROTO_DIR"/*.proto

echo "Generated Swift sources in $OUT_DIR"
