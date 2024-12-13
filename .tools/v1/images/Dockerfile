# Stage 1: Build OpenTofu or download the binary
FROM alpine:latest AS builder

# Set OpenTofu version
ARG OPENTOFU_VERSION=0.2.0

# Install curl to download the binary
RUN apk add --no-cache curl

# Download the OpenTofu binary
RUN curl -Lo /opentofu "https://releases.opentofu.org/releases/${OPENTOFU_VERSION}/opentofu-linux-amd64" \
    && chmod +x /opentofu

# Stage 2: Create a minimal final image with only the binary
FROM gcr.io/distroless/static:nonroot

# Copy the OpenTofu binary from the builder
COPY --from=builder /opentofu /usr/local/bin/opentofu

# Create a working directory for mounting volumes
WORKDIR /data

# Set opentofu as the default command
ENTRYPOINT ["/usr/local/bin/opentofu"]
