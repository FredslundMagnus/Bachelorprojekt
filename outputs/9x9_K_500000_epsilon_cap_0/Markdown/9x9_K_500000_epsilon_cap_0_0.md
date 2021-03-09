
# Parameters

    Name :                      9x9_K_500000_epsilon_cap_0-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    K :                         500000.0
    Epsilon cap :               0.0
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      25385999377 function calls (25255926038 primitive calls) in 35686.10 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35704.248 35704.248 {built-in method builtins.exec}
                      1    0.762    0.762 35704.248 35704.248 <string>:1(<module>)
                      1  129.781  129.781 35703.486 35703.486 main.py:10(teleport)
                4645724   20.049    0.000 13387.454    0.003 agent.py:26(learn)
                4645724  323.786    0.000 11432.600    0.002 learner.py:42(Qlearn)
                2322862   11.513    0.000 9059.335    0.004 game.py:21(step)
                2322862   14.984    0.000 8513.604    0.004 layers.py:212(step)
                2322862   79.454    0.000 7991.222    0.003 agent.py:50(_learn)
        146331700/16259372  625.494    0.000 5634.588    0.000 module.py:715(_call_impl)
                2322862  204.757    0.000 5567.087    0.002 layers.py:17(step)
                2322862   69.144    0.000 5366.085    0.002 agent.py:101(_learn)
              232286200  256.949    0.000 5339.120    0.000 layer.py:66(move)
               11613648   29.332    0.000 5241.469    0.000 network.py:24(forward)
               11613648  142.638    0.000 5136.147    0.000 container.py:115(forward)
                4645724   30.396    0.000 4542.049    0.001 grad_mode.py:23(decorate_context)
                4645724  161.954    0.000 4455.834    0.001 adam.py:55(step)
                4645724  817.335    0.000 3639.790    0.001 functional.py:53(adam)
                2322862 1793.283    0.001 3500.318    0.002 agent.py:77(interveen)
                4645062  119.090    0.000 3456.786    0.001 agent.py:45(__call__)
                2322862 1941.199    0.001 3418.082    0.001 replaybuffer.py:27(teleporter_save_data)
                2322863  231.305    0.000 2908.135    0.001 layers.py:192(update)
              232286200  529.198    0.000 2727.227    0.000 layers.py:229(check)
                4645724   29.223    0.000 2706.451    0.001 tensor.py:181(backward)
                4645724   18.869    0.000 2677.228    0.001 __init__.py:68(backward)
                4645724 2549.424    0.001 2549.424    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2322862 1460.198    0.001 2528.583    0.001 replaybuffer.py:23(sample_data)
              232286200  350.123    0.000 2073.779    0.000 layers.py:223(isFree)
                2322862  888.986    0.000 1891.228    0.001 agent.py:59(modify)
               23227296   39.214    0.000 1870.335    0.000 conv.py:422(forward)
               23227296   48.379    0.000 1812.473    0.000 conv.py:414(_conv_forward)
               23227296 1755.336    0.000 1755.336    0.000 {built-in method conv2d}
             1592387504 1487.253    0.000 1723.656    0.000 layer.py:63(isFree)
               30195220   67.198    0.000 1641.437    0.000 linear.py:92(forward)
               30195220  121.351    0.000 1539.580    0.000 functional.py:1669(linear)
              108456039 1196.688    0.000 1196.688    0.000 {built-in method clone}
              292680666  693.112    0.000 1162.327    0.000 tensor.py:933(grad)
               18582904  422.041    0.000 1135.663    0.000 layer.py:90(update)
               30195220 1077.695    0.000 1077.695    0.000 {built-in method addmm}
                2322862   34.956    0.000 1067.499    0.000 agent.py:96(__call__)
               18582234 1058.608    0.000 1058.608    0.000 {built-in method cat}
                6967924   49.587    0.000 1037.747    0.000 agent.py:54(modify_board)
                4645724   95.836    0.000 1008.729    0.000 optimizer.py:167(zero_grad)
              232286200  610.464    0.000  977.750    0.000 layers.py:124(check)
                2322862   42.313    0.000  881.496    0.000 replaybuffer.py:19(stacker)
                1175999   15.872    0.000  821.550    0.001 layers.py:233(restart)
                9550013  750.465    0.000  750.465    0.000 {built-in method tensor}
               83623032  741.417    0.000  741.417    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               41808868   37.979    0.000  714.683    0.000 activation.py:713(forward)
                1175999    3.395    0.000  692.561    0.001 levels.py:8(__init__)
                1175999   11.872    0.000  689.166    0.001 level.py:8(__init__)
               41808868   56.886    0.000  676.704    0.000 functional.py:1292(leaky_relu)
                6967924  666.535    0.000  666.535    0.000 {built-in method torch._C._nn.one_hot}
              241579598   73.685    0.000  660.957    0.000 {built-in method builtins.all}
                1602652  104.945    0.000  657.670    0.000 levels.py:11(generate)
              373980326  208.661    0.000  621.281    0.000 overrides.py:1070(has_torch_function)
               41808868  614.165    0.000  614.165    0.000 {built-in method torch._C._nn.leaky_relu}
               83623032  609.998    0.000  609.998    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              704062146  169.598    0.000  608.871    0.000 layers.py:197(<genexpr>)
                4645724    6.219    0.000  605.064    0.000 game.py:17(board)
              674237524  576.535    0.000  576.535    0.000 layer.py:85(elements)
             1976204490  376.327    0.000  542.640    0.000 enum.py:646(__hash__)
              232286200  286.013    0.000  446.677    0.000 layers.py:95(check)
                2322862  247.785    0.000  426.207    0.000 collector.py:37(collect)
               41811516  424.880    0.000  424.880    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              232286300  286.417    0.000  416.371    0.000 layers.py:65(isDone)
              413466995  158.232    0.000  392.149    0.000 {built-in method builtins.any}
               41811516  386.151    0.000  386.151    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4645062  131.340    0.000  362.764    0.000 exploration.py:53(softmaxer)
              232286200  256.714    0.000  362.493    0.000 layers.py:50(check)
             3621046556  359.707    0.000  359.707    0.000 layer.py:59(positions)
               41811516  346.408    0.000  346.408    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              115423963  344.883    0.000  344.883    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              232286200  222.594    0.000  333.817    0.000 layers.py:77(check)
               41811516  300.665    0.000  300.665    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9293298   44.851    0.000  274.176    0.000 tensor.py:21(wrapped)
                4645724    7.809    0.000  253.180    0.000 loss.py:445(forward)
                4645724   30.908    0.000  245.371    0.000 functional.py:2637(mse_loss)
               41811516  235.156    0.000  235.156    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              787448706  185.276    0.000  230.470    0.000 overrides.py:1083(<genexpr>)
                1602652  117.829    0.000  222.337    0.000 levels.py:76(RFS)
                6704165   83.612    0.000  217.919    0.000 random.py:315(sample)
              319168782  151.443    0.000  202.725    0.000 layer.py:76(add)
               30195220  200.646    0.000  200.646    0.000 {method 't' of 'torch._C._TensorBase' objects}
              251585328  139.832    0.000  199.543    0.000 layer.py:72(remove)
               13937172  172.580    0.000  172.580    0.000 {built-in method sum}
             1976221593  166.316    0.000  166.316    0.000 {built-in method builtins.hash}
                3527997   21.338    0.000  156.419    0.000 level.py:41(notUsed)
                6968586   33.758    0.000  151.541    0.000 tensor.py:506(__rsub__)
             1393965777  142.789    0.000  142.789    0.000 layer.py:125(isBlocking)
                4645724  137.591    0.000  137.591    0.000 {built-in method torch._C._nn.mse_loss}
                6968586  132.709    0.000  132.709    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               23227296   17.184    0.000  127.192    0.000 flatten.py:39(forward)
        403023101/403023099   59.863    0.000  126.232    0.000 {built-in method builtins.len}
                4646420  126.129    0.000  126.129    0.000 {built-in method max}
               41811606   53.790    0.000  120.111    0.000 tensor.py:596(__hash__)
                6968586  117.784    0.000  117.784    0.000 {built-in method rsub}
                4645062  112.907    0.000  112.907    0.000 {built-in method multinomial}
               23227296  110.007    0.000  110.007    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              154602303   75.218    0.000  109.881    0.000 random.py:250(_randbelow_with_getrandbits)
                9407992   16.028    0.000  109.646    0.000 layer.py:40(restart)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9395476: <9x9_K_500000_epsilon_cap_0_0> in cluster <dcc> Done

Job <9x9_K_500000_epsilon_cap_0_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Tue Mar  9 00:59:03 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Mar  9 01:04:50 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar  9 01:04:50 2021
Terminated at Tue Mar  9 11:00:12 2021
Results reported at Tue Mar  9 11:00:12 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35619.84 sec.
    Max Memory :                                 2402 MB
    Average Memory :                             2384.06 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5790.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35710 sec.
    Turnaround time :                            36069 sec.

The output (if any) is above this job summary.

