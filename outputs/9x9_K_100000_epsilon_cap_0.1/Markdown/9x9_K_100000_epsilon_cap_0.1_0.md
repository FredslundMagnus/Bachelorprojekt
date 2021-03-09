
# Parameters

    Name :                      9x9_K_100000_epsilon_cap_0.1-0
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
    K :                         100000.0
    Epsilon cap :               0.1
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


      23948025934 function calls (23823432039 primitive calls) in 35694.98 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.988 35710.988 {built-in method builtins.exec}
                      1    0.715    0.715 35710.988 35710.988 <string>:1(<module>)
                      1   98.464   98.464 35710.273 35710.273 main.py:10(teleport)
                4449946   16.271    0.000 14992.096    0.003 agent.py:26(learn)
                4449946  358.401    0.000 12992.333    0.003 learner.py:42(Qlearn)
                2224973   72.590    0.000 8933.234    0.004 agent.py:50(_learn)
                2224973    8.726    0.000 6923.070    0.003 game.py:21(step)
                2224973   10.140    0.000 6393.808    0.003 layers.py:212(step)
                2224973   63.425    0.000 6033.887    0.003 agent.py:101(_learn)
        140167228/15574344  548.433    0.000 5921.665    0.000 module.py:715(_call_impl)
               11124398   29.474    0.000 5544.283    0.000 network.py:24(forward)
                4449946   25.629    0.000 5536.391    0.001 grad_mode.py:23(decorate_context)
                4449946  145.145    0.000 5460.737    0.001 adam.py:55(step)
               11124398  138.092    0.000 5451.963    0.000 container.py:115(forward)
                4449946  995.446    0.000 4674.110    0.001 functional.py:53(adam)
                2224973  150.383    0.000 4197.112    0.002 layers.py:17(step)
                2224973 2176.751    0.001 4118.122    0.002 replaybuffer.py:27(teleporter_save_data)
              222497300  223.873    0.000 4027.329    0.000 layer.py:66(move)
                2224973 2117.491    0.001 3930.087    0.002 agent.py:77(interveen)
                4449479  101.168    0.000 3624.167    0.001 agent.py:45(__call__)
                4449946   28.398    0.000 2956.528    0.001 tensor.py:181(backward)
                4449946   15.142    0.000 2928.131    0.001 __init__.py:68(backward)
                4449946 2798.292    0.001 2798.292    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              222497300  460.255    0.000 2275.606    0.000 layers.py:229(check)
                2224974  194.542    0.000 2172.098    0.001 layers.py:192(update)
                2224973  940.936    0.000 1979.994    0.001 agent.py:59(modify)
               22248796   38.235    0.000 1966.681    0.000 conv.py:422(forward)
               22248796   49.647    0.000 1914.261    0.000 conv.py:414(_conv_forward)
               22248796 1856.154    0.000 1856.154    0.000 {built-in method conv2d}
               28923248   65.667    0.000 1778.830    0.000 linear.py:92(forward)
                2224973  743.188    0.000 1768.545    0.001 replaybuffer.py:23(sample_data)
               28923248  111.933    0.000 1683.800    0.000 functional.py:1669(linear)
              111262191 1546.978    0.000 1546.978    0.000 {built-in method clone}
              222497300  305.763    0.000 1319.043    0.000 layers.py:223(isFree)
               28923248 1204.503    0.000 1204.503    0.000 {built-in method addmm}
              280346652  768.777    0.000 1197.924    0.000 tensor.py:933(grad)
                4449946  109.742    0.000 1151.497    0.000 optimizer.py:167(zero_grad)
                2224973   29.030    0.000 1109.225    0.000 agent.py:96(__call__)
                6674452   44.565    0.000 1078.858    0.000 agent.py:54(modify_board)
               17799317 1075.561    0.000 1075.561    0.000 {built-in method cat}
             1415158736  821.609    0.000 1013.280    0.000 layer.py:63(isFree)
               80099028  980.194    0.000  980.194    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2224973   39.037    0.000  874.374    0.000 replaybuffer.py:19(stacker)
               80099028  830.313    0.000  830.313    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               40047646   37.865    0.000  815.453    0.000 activation.py:713(forward)
              222497300  479.140    0.000  787.119    0.000 layers.py:124(check)
               40047646   54.036    0.000  777.588    0.000 functional.py:1292(leaky_relu)
               40047646  718.374    0.000  718.374    0.000 {built-in method torch._C._nn.leaky_relu}
                9171165  715.392    0.000  715.392    0.000 {built-in method tensor}
                1126407   10.913    0.000  696.915    0.001 layers.py:233(restart)
                6674452  678.623    0.000  678.623    0.000 {built-in method torch._C._nn.one_hot}
               17799792  263.867    0.000  674.126    0.000 layer.py:90(update)
                1126407    2.268    0.000  591.924    0.001 levels.py:8(__init__)
                1126407    8.261    0.000  589.655    0.001 level.py:8(__init__)
                1536267   89.679    0.000  565.573    0.000 levels.py:11(generate)
              358220698  190.992    0.000  562.835    0.000 overrides.py:1070(has_torch_function)
              231399038   65.328    0.000  560.148    0.000 {built-in method builtins.all}
                4449946    5.176    0.000  558.746    0.000 game.py:17(board)
               40049514  538.401    0.000  538.401    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2224973  305.962    0.000  516.710    0.000 collector.py:37(collect)
              673141800  155.202    0.000  513.318    0.000 layers.py:197(<genexpr>)
               40049514  481.943    0.000  481.943    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1892817641  338.078    0.000  480.323    0.000 enum.py:646(__hash__)
              117936643  477.446    0.000  477.446    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               40049514  441.169    0.000  441.169    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               40049514  394.662    0.000  394.662    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                4449479  137.223    0.000  384.163    0.000 exploration.py:53(softmaxer)
              222497300  246.426    0.000  379.955    0.000 layers.py:95(check)
              396043839  142.079    0.000  348.978    0.000 {built-in method builtins.any}
              222497400  223.775    0.000  338.848    0.000 layers.py:65(isDone)
               40049514  321.766    0.000  321.766    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              613508085  303.540    0.000  303.540    0.000 layer.py:85(elements)
             3436874219  296.947    0.000  296.947    0.000 layer.py:59(positions)
              222497300  194.991    0.000  290.150    0.000 layers.py:50(check)
              222497300  186.874    0.000  287.940    0.000 layers.py:77(check)
                8901638   40.687    0.000  269.313    0.000 tensor.py:21(wrapped)
                4449946    7.637    0.000  250.389    0.000 loss.py:445(forward)
                4449946   23.586    0.000  242.752    0.000 functional.py:2637(mse_loss)
               28923248  236.943    0.000  236.943    0.000 {method 't' of 'torch._C._TensorBase' objects}
               13349838  208.011    0.000  208.011    0.000 {built-in method sum}
              754265838  163.605    0.000  203.976    0.000 overrides.py:1083(<genexpr>)
                1536267  101.131    0.000  192.730    0.000 levels.py:76(RFS)
                6423914   67.532    0.000  176.212    0.000 random.py:315(sample)
                6674919   33.140    0.000  161.899    0.000 tensor.py:506(__rsub__)
              289520107  116.218    0.000  155.536    0.000 layer.py:76(add)
                4449946  152.088    0.000  152.088    0.000 {built-in method torch._C._nn.mse_loss}
              224813795  104.434    0.000  151.677    0.000 layer.py:72(remove)
               22248796   15.556    0.000  149.764    0.000 flatten.py:39(forward)
             1892834024  142.247    0.000  142.247    0.000 {built-in method builtins.hash}
                6674919  142.008    0.000  142.008    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                4450612  136.857    0.000  136.857    0.000 {built-in method max}
                3379221   17.979    0.000  135.384    0.000 level.py:41(notUsed)
               22248796  134.207    0.000  134.207    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
        386063879/386063877   62.400    0.000  129.930    0.000 {built-in method builtins.len}
              142393089  129.236    0.000  129.236    0.000 {built-in method torch._C._get_tracing_state}
                6674919  128.759    0.000  128.759    0.000 {built-in method rsub}
                4449479  123.727    0.000  123.727    0.000 {built-in method multinomial}
             1241386328  122.457    0.000  122.457    0.000 layer.py:125(isBlocking)
                4449946  111.238    0.000  111.238    0.000 {built-in method gather}
                4449946   18.962    0.000  110.904    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9395473: <9x9_K_100000_epsilon_cap_0.1_0> in cluster <dcc> Done

Job <9x9_K_100000_epsilon_cap_0.1_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Tue Mar  9 00:59:02 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Mar  9 00:59:20 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar  9 00:59:20 2021
Terminated at Tue Mar  9 10:54:55 2021
Results reported at Tue Mar  9 10:54:55 2021

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

    CPU time :                                   35590.32 sec.
    Max Memory :                                 2387 MB
    Average Memory :                             2377.89 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5805.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35731 sec.
    Turnaround time :                            35753 sec.

The output (if any) is above this job summary.

