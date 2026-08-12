#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
21st.dev Magic MCP Bridge Client (ui-ux-pro-max/scripts/magic_21st.py)

A lightweight CLI bridge that allows AI coding agents (such as Arena Agent Mode, Claude Code CLI,
or CI/CD pipelines) to query the @21st-dev/magic MCP server via standard JSON-RPC over stdio.

Usage:
    export API_KEY="your_21st_api_key"
    
    # 1. List available tools from the 21st.dev MCP server:
    python3 magic_21st.py --list-tools

    # 2. Call a specific tool (e.g., search or get component):
    python3 magic_21st.py --call 21st_magic_search --args '{"query": "navbar modern"}'
    python3 magic_21st.py --call 21st_magic_component --args '{"component_id": "example/navbar"}'
"""

import os
import sys
import json
import argparse
import subprocess

def run_mcp_request(method: str, params: dict, api_key: str):
    """Sends a JSON-RPC request to @21st-dev/magic via npx over stdio."""
    env = os.environ.copy()
    if api_key:
        env["API_KEY"] = api_key
        env["TWENTY_FIRST_API_KEY"] = api_key

    try:
        process = subprocess.Popen(
            ["npx", "-y", "@21st-dev/magic@latest"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env
        )
    except Exception as e:
        print(f"[ERROR] Failed to launch npx @21st-dev/magic: {e}", file=sys.stderr)
        sys.exit(1)

    # 1. Send initialize handshake
    init_req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "ui-ux-pro-max-magic-client", "version": "1.0.0"}
        }
    }
    
    process.stdin.write(json.dumps(init_req) + "\n")
    process.stdin.flush()
    init_resp_line = process.stdout.readline()
    if not init_resp_line:
        err = process.stderr.read()
        print(f"[ERROR] No initialize response received from MCP server.\nStderr: {err}", file=sys.stderr)
        process.terminate()
        sys.exit(1)

    try:
        init_resp = json.loads(init_resp_line)
        if "error" in init_resp:
            print(f"[ERROR] Authentication / MCP Error during initialize:\n{json.dumps(init_resp['error'], indent=2)}", file=sys.stderr)
            process.terminate()
            sys.exit(1)
    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON in init response: {init_resp_line}", file=sys.stderr)
        process.terminate()
        sys.exit(1)

    # 2. Send initialized notification
    notify_req = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized",
        "params": {}
    }
    process.stdin.write(json.dumps(notify_req) + "\n")
    process.stdin.flush()

    # 3. Send target method request
    target_req = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": method,
        "params": params
    }
    process.stdin.write(json.dumps(target_req) + "\n")
    process.stdin.flush()
    process.stdin.close()

    target_resp_line = process.stdout.readline()
    process.terminate()

    if not target_resp_line:
        print("[ERROR] Empty response from MCP server.", file=sys.stderr)
        sys.exit(1)

    try:
        resp = json.loads(target_resp_line)
        return resp
    except json.JSONDecodeError:
        print(f"[ERROR] Could not parse JSON response: {target_resp_line}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Bridge CLI to query @21st-dev/magic MCP Server")
    parser.add_argument("--list-tools", action="store_true", help="List available tools on the 21st.dev MCP server")
    parser.add_argument("--call", type=str, help="Name of the MCP tool to call (e.g., 21st_magic_search)")
    parser.add_argument("--args", type=str, default="{}", help="JSON string of arguments for the tool call")
    parser.add_argument("--api-key", type=str, default=os.environ.get("API_KEY", ""), help="21st.dev API Key")

    args = parser.parse_args()

    if not args.api_key:
        print("[WARNING] No API_KEY provided. Set export API_KEY='your_key' or pass --api-key.", file=sys.stderr)

    if args.list_tools:
        result = run_mcp_request("tools/list", {}, args.api_key)
        print(json.dumps(result, indent=2))
        return

    if args.call:
        try:
            params = json.loads(args.args)
        except json.JSONDecodeError:
            print("[ERROR] --args must be a valid JSON string", file=sys.stderr)
            sys.exit(1)

        result = run_mcp_request("tools/call", {"name": args.call, "arguments": params}, args.api_key)
        print(json.dumps(result, indent=2))
        return

    parser.print_help()

if __name__ == "__main__":
    main()
