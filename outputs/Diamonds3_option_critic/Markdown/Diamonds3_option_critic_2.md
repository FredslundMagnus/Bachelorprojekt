
# Parameters

    Name :                      Diamonds3_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal6
    Failed actions chance :     0.0
    Hours :                     72.0
    Batch :                     25
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      53616146497 function calls (51917255595 primitive calls) in 258900.54 seconds

##    Ordered by: cumulative time
   List reduced from 428 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.538 258900.538 {built-in method builtins.exec}
                      1    0.385    0.385 258900.538 258900.538 <string>:1(<module>)
                      1 6428.551 6428.551 258900.153 258900.153 optionCritic.py:195(option_critic_run)
               60415725 9415.483    0.000 113105.310    0.002 optionCritic.py:143(actor_loss_fn)
        2243610675/552574530 9994.302    0.000 112805.146    0.000 module.py:866(_call_impl)
              187892905  812.795    0.000 105150.895    0.001 optionCritic.py:70(get_state)
              187892905 2266.365    0.000 101798.337    0.001 container.py:117(forward)
                2416629   21.004    0.000 71990.526    0.030 tensor.py:195(backward)
                2416629   26.236    0.000 71969.209    0.030 __init__.py:68(backward)
                2416629 71885.084    0.030 71885.084    0.030 {method 'run_backward' of 'torch._C._EngineBase' objects}
              375785810  977.129    0.000 64463.377    0.000 conv.py:398(forward)
              375785810  522.842    0.000 63091.870    0.000 conv.py:390(_conv_forward)
              375785810 62569.028    0.000 62569.028    0.000 {built-in method conv2d}
              740467435 1627.765    0.000 21550.286    0.000 linear.py:93(forward)
               60415725 3699.622    0.000 21537.970    0.000 optionCritic.py:91(get_action)
              740467435  645.049    0.000 19236.783    0.000 functional.py:1737(linear)
              740467435 18436.774    0.000 18436.774    0.000 {built-in method torch._C._nn.linear}
               60415725 1240.988    0.000 14567.047    0.000 optionCritic.py:80(predict_option_termination)
              120831450 1291.009    0.000 8233.740    0.000 distribution.py:34(__init__)
                2416629   61.364    0.000 7681.421    0.003 optimizer.py:84(wrapper)
                2416629   31.770    0.000 7469.896    0.003 grad_mode.py:24(decorate_context)
                2416629  141.229    0.000 7381.344    0.003 rmsprop.py:56(step)
              563678715  528.921    0.000 7371.881    0.000 activation.py:713(forward)
               60415725  611.212    0.000 7121.244    0.000 categorical.py:115(log_prob)
                2416629  142.497    0.000 7085.123    0.003 _functional.py:203(rmsprop)
              563678715  549.766    0.000 6842.960    0.000 functional.py:1364(leaky_relu)
              563678715 6182.072    0.000 6182.072    0.000 {built-in method torch._C._nn.leaky_relu}
               60415725  824.574    0.000 6039.361    0.000 categorical.py:49(__init__)
               60415725  505.968    0.000 5760.206    0.000 bernoulli.py:34(__init__)
              182830293  381.061    0.000 5638.618    0.000 optionCritic.py:77(get_Q)
                 604157   99.045    0.000 5093.732    0.008 optionCritic.py:116(critic_loss_fn)
              121435607  407.412    0.000 4400.340    0.000 optionCritic.py:88(get_terminations)
                2416629   12.614    0.000 4086.614    0.002 game.py:41(step)
                2416629   23.563    0.000 3931.924    0.002 layers.py:718(step)
               60415725 2479.457    0.000 3664.230    0.000 constraints.py:398(check)
               33832800 3237.596    0.000 3237.596    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               60415725  502.096    0.000 2897.119    0.000 distribution.py:240(_validate_sample)
                2416629   90.176    0.000 2330.539    0.001 layers.py:17(step)
               33832800 2305.109    0.000 2305.109    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               60415725  471.947    0.000 2242.476    0.000 bernoulli.py:86(sample)
               60415725  151.524    0.000 2232.735    0.000 layer.py:98(move)
              187892905  224.076    0.000 2097.664    0.000 activation.py:101(forward)
               60415725 2080.487    0.000 2080.487    0.000 constraints.py:364(check)
               60415725 1035.033    0.000 1979.557    0.000 categorical.py:123(entropy)
              187892905  205.856    0.000 1873.587    0.000 functional.py:1195(relu)
               60415725 1867.645    0.000 1867.645    0.000 constraints.py:249(check)
             2906226701 1833.084    0.000 1833.270    0.000 module.py:934(__getattr__)
              422910075 1814.402    0.000 1814.402    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              181247175  250.473    0.000 1777.976    0.000 utils.py:106(__get__)
              187892905 1639.127    0.000 1639.127    0.000 {built-in method relu}
              187892905  174.243    0.000 1634.421    0.000 flatten.py:39(forward)
              182455489  197.686    0.000 1601.454    0.000 tensor.py:525(__rsub__)
              120831450  577.910    0.000 1577.464    0.000 functional.py:46(broadcast_tensors)
                 604157 1312.047    0.002 1571.798    0.003 replaybuffer.py:42(sample_option_critic)
                2416630  206.516    0.000 1568.975    0.001 layers.py:684(update)
               26582919   62.021    0.000 1519.125    0.000 tensor.py:575(__iter__)
              187892905 1460.178    0.000 1460.178    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               60415725  284.077    0.000 1422.220    0.000 layers.py:735(check)
               26582919 1419.931    0.000 1419.931    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               60415725  397.380    0.000 1406.180    0.000 categorical.py:108(sample)
              182455489 1374.256    0.000 1374.256    0.000 {built-in method rsub}
               60415725  303.505    0.000 1357.307    0.000 utils.py:11(broadcast_all)
               60415725   73.746    0.000 1342.640    0.000 categorical.py:88(logits)
               60415725   80.211    0.000 1268.895    0.000 utils.py:82(probs_to_logits)
              121435607 1266.275    0.000 1266.275    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              181247175 1237.361    0.000 1237.361    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             2270193594 1234.851    0.000 1234.851    0.000 {built-in method torch._C._get_tracing_state}
              181851332 1230.767    0.000 1230.767    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             9767298300 1155.406    0.000 1172.803    0.000 {built-in method builtins.len}
              181247175 1021.349    0.000 1021.349    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               60415725  945.252    0.000  945.252    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
             9162335605  940.884    0.000  940.884    0.000 {method 'values' of 'collections.OrderedDict' objects}
              120831450  835.888    0.000  835.888    0.000 {built-in method broadcast_tensors}
                2416629   89.286    0.000  808.470    0.000 replaybuffer.py:34(save_option_critic)
                2416629  110.563    0.000  779.275    0.000 optimizer.py:189(zero_grad)
               60415725  157.569    0.000  746.924    0.000 utils.py:77(clamp_probs)
              183059646  662.746    0.000  662.746    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               60415725  643.605    0.000  643.605    0.000 {built-in method bernoulli}
               33832800  595.684    0.000  595.684    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               60415725  594.445    0.000  594.445    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               60415725  589.355    0.000  589.355    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               60790529  573.194    0.000  573.194    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               12321678  252.609    0.000  541.334    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               60415725  112.797    0.000  537.533    0.000 layers.py:729(isFree)
              363702664  533.795    0.000  533.795    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               33832800  526.058    0.000  526.058    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              120831450  525.628    0.000  525.628    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               19333040  307.435    0.000  513.496    0.000 layer.py:167(NoRock_update)
               60415725  507.449    0.000  507.449    0.000 {built-in method clamp}
               16312249  500.232    0.000  500.232    0.000 {built-in method tensor}
              181247200  141.739    0.000  475.956    0.000 {built-in method builtins.all}
               60415725  441.760    0.000  441.760    0.000 {built-in method log}
              797863247  286.439    0.000  433.002    0.000 {built-in method builtins.isinstance}
               60415725  425.952    0.000  425.952    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              372813990  363.630    0.000  424.736    0.000 layer.py:95(isFree)
              181626835  401.205    0.000  401.205    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               60415725  399.306    0.000  399.306    0.000 {built-in method all}
               33832786  397.562    0.000  397.562    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              187892919  394.542    0.000  394.542    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                7249891   15.936    0.000  390.538    0.000 game.py:37(board)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601865: <Diamonds3_option_critic_2> in cluster <dcc> Done

Job <Diamonds3_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:10 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:12 2021
Terminated at Sun May  2 21:36:15 2021
Results reported at Sun May  2 21:36:15 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258286.44 sec.
    Max Memory :                                 911 MB
    Average Memory :                             887.82 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15473.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258916 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

