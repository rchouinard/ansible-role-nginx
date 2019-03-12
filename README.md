# NGINX Ansible Role

This role provides the NGINX web server.

## Requirements

* Ansible 2.4+

## Role Variables

``` yaml
nginx_user: nginx
nginx_group: ~
nginx_worker_processes: auto
nginx_worker_rlimit_nofile: 8192
nginx_worker_connections: 8000
nginx_http_server_tokens: 'off'
nginx_http_autoindex: 'off'
nginx_http_charset: utf-8
nginx_http_sendfile: 'on'
nginx_http_tcp_nopush: 'on'
nginx_http_tcp_nodelay: 'on'
nginx_http_keepalive_timeout: 20s
nginx_http_gzip: 'on'
nginx_http_gzip_comp_level: 5
nginx_http_gzip_min_length: 256
nginx_http_gzip_proxied: any
nginx_http_gzip_vary: 'on'
nginx_http_gzip_static: 'off'
nginx_http_ssl_session_timeout: 1d
nginx_http_ssl_session_cache: shared:SSL:50m
nginx_http_ssl_session_tickets: 'off'
nginx_http_ssl_protocols: TLSv1.2
nginx_http_ssl_ciphers: ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256
nginx_http_ssl_prefer_server_ciphers: 'on'
nginx_http_ssl_stapling: 'on'
nginx_http_ssl_stapling_verify: 'on'
nginx_http_resolver: 8.8.8.8 8.8.4.4 [2001:4860:4860::8888] [2001:4860:4860::8844] valid=3600s
nginx_http_resolver_timeout: 2s
```

## Dependencies

None.

## Example Playbook

``` yaml
- hosts: localhost
  roles:
    - rchouinard.nginx
```

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
