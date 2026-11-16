---
name: tailscale-serve-sharing
description: Share a page or server running on this computer with the user's own devices (phone, tablet, another computer) through Tailscale Serve, inside the user's tailnet only, without changing any Serve entry that already exists. Use when the user wants to open a local page, dev server or build on another device, at home or away, or asks to serve something with Tailscale.
---

# Tailscale Serve Sharing

Tailscale Serve gives a local server an address such as
`https://<machine>.<tailnet>.ts.net:8443` that only the user's signed-in
Tailscale devices can open, wherever they are. The computer's Serve
configuration is shared. Its other entries belong to the user or to other
programs, for example the address the user's phone uses to reach an app on this
computer. A Serve command replaces an entry on the same port without asking, and
nothing in its output says that it did.

This happened: asked to "serve this with Tailscale", an agent ran
`tailscale serve --bg --https=443 http://127.0.0.1:4731` without reading the
configuration first. That replaced the entry on 443 that the user's phone used
to reach his app, and turning the share off later removed it completely. The
phone lost the app.

So: read the configuration first, add exactly one new entry on a port nobody
uses, remove only that entry, and show that every other entry is as it was.

## Rules

- **Read before you change.** Save `tailscale serve status --json` before your
  first Serve command. An entry you did not add in this task is someone
  else's, however unused or stale it looks.
- **Always name the port, and never use 443.** `tailscale serve --bg 4731`
  without `--https=<port>` takes HTTPS port 443, the computer's default
  address, which the user's own apps use.
- **Use only a port the status does not show.** Never add a path
  (`--set-path`) or anything else to an existing entry: that changes it.
- **Never run** `tailscale serve reset`, `tailscale serve clear`, or
  `tailscale funnel`. The first two remove every entry; Funnel puts the server
  on the public internet. Do not change Tailscale's own settings (`tailscale
  up`, `tailscale set`, logging in or out).
- **Turn off only the entry you added.** An entry of someone else's that looks
  wrong or dead is reported to the user, not removed or "tidied".
- **Keep the local server on `127.0.0.1`.** Serve reaches it there. Binding it
  to all addresses (`0.0.0.0`, `--host`) also opens it to the local network;
  do not do that, or change the firewall or sharing settings, for this.

When the request can only be met by breaking a rule (the user asks for port
443, for a public link, or to remove someone else's entry), tell the user what
it would change and do it only on their explicit word.

## Share

1. **Before.** Check that Tailscale runs (`tailscale status`). If it does not,
   tell the user; do not start it or log in. Save the configuration to a file
   in your task folder, for example
   `tailscale serve status --json > serve-before.json`, and note each
   existing entry's address. Request each one once (`curl -sS -o /dev/null
   -w '%{http_code}\n' <address>`) so you know what it answers now; an
   AutoByteus node answers on `<address>/rest/health`.
2. **Port.** Pick a port that is not 443 and not in the saved status: 8443 if
   free, otherwise 8444, 8445 and so on.
3. **Add.** `tailscale serve --bg --https=<port> http://127.0.0.1:<local-port>`.
4. **Compare.** Read `tailscale serve status --json` again. Every entry from
   the before file must still be there with the same target, and the only
   new one is yours. If anything else differs, go to Recovery now.
5. **Check.** Open `https://<machine>.<tailnet>.ts.net:<port>/` from this
   computer and request the other entries again; each answers as before. A dev
   server may refuse the unknown host name (Vite: `server.allowedHosts`); allow
   the `.ts.net` name for this run, and say what you changed.
6. **Tell the user:** the address; that only their signed-in Tailscale devices
   can open it, at home or away; that it works while this computer is awake and
   the server runs; that the other entries (name them) are unchanged; and how to
   turn it off (`tailscale serve --https=<port> off`, or ask you).

## Turn off

When the user is done with it, or your task ends and the user did not ask to
keep it:

1. `tailscale serve --https=<port> off` for your port only.
2. Read `tailscale serve status --json` and compare it with the before file:
   it must be the same. Request the other entries once more.
3. Stop the local server if you started it for this.
4. Tell the user it is off and that the other entries are as they were. If you
   leave the share on, your report says so, with its address and how to turn it
   off.

## Recovery

If an entry from the before file is missing or changed:

- **Your command did it:** restore exactly that entry from the before file at
  once, with its own port and target (for a proxy:
  `tailscale serve --bg --https=<its port> <its target>`), compare again, and
  tell the user what happened and that it is restored.
- **You did not do it, or you cannot tell:** change nothing more. Tell the user
  at once, with the before and current status.
